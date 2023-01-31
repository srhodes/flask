from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Book(db.Model):
    """Book"""

    __tablename__ = "books"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    autho = db.Column(db.String(50),
                        nullable=False,
                        unique=True)
    price = db.Column(db.Float(2))
    page_count = db.Column(db.Integer)
    publisher = db.Column(db.String(50))
    publication_date = db.Column(db.Date)



