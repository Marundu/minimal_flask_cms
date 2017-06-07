from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from app import app, db
from models import Pages

@app.route('/')
def index():
    pages=db.session.query(Pages).all()
    return render_template('index.html', pages=pages)

@app.route('/page/<int:page_id>')
def view_page(page_id):
    page=db.session.query(Pages).filter_by(id=page_id).first()
    return render_template('page.html',
                            id=page.id,
                            title=page.title,
                            content=page.content
                            )

@app.route('/edit-page/<int:page_id>')
def edit_page(page_id):
    page=db.session.query(Pages).filter_by(id=page_id).first()
    return render_template('edit-page.html',
                            id=page.id,
                            title=page.title,
                            content=page.content
                            )

@app.route('/update-page/', methods=['POST'])
def update_page():
    page_id=request.form['id']
    title=request.form['title']
    content=request.form['content']
    db.session.query(Pages).filter_by(id=page_id).update({'title': title, 'content': content})
    
    db.session.commit()
    return redirect('/page/' + page_id)

@app.route('/new-page/')
def new_page():
    return render_template('new-page.html')

@app.route('/save-page/', methods=['POST'])
def save_page():
    page=Pages(title=request.form['title'],
               content=request.form['content'])
    
    db.session.add(page)
    db.session.commit()
    
    return redirect('/page/{}'.format(page.id))

@app.route('/delete-page/<int:page_id>')
def delete_page(page_id):
    db.session.query(Pages).filter_by(id=page_id).delete()
    db.session.commit()
    return redirect('/')                                                                     
