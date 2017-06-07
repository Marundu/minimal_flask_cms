from app import db

class Pages(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(1000))
    content=db.Column(db.BLOB)
    
    def __init__(self, title, content):
        self.title=title
        self.content=content
    
    def __repr__(self):
        return '<Pages: id={}, title={}, content={}>'.format(self.id, self.title, self.content)
