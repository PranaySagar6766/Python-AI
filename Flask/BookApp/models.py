from . import db


class Book(db.Model):
    id     = db.Column(db.Integer,     primary_key=True)
    title  = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price  = db.Column(db.Float,       nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


class User(db.Model):
    id       = db.Column(db.Integer,     primary_key=True)
    username = db.Column(db.String(20),  unique=True,  nullable=False)
    email    = db.Column(db.String(120), unique=True,  nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"