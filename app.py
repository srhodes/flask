from flask import Flask
from models import db, connect_db, Book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

book = Book(autho="Stephan", page_count=10)

with app.app_context():
    db.session.add(book)
    db.session.commit()

@app.route('/')
def say_hello():
    return"<html><body><h1>Hello</h1></body></html>"