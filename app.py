from flask import Flask
from models import db, connect_db, Book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

app.app_context().push()
book = Book(autho="Stephan", page_count=10)

db.session.add(book)
db.session.commit()

@app.route('/')
def say_hello():
    return"<html><body><h1>Hello</h1></body></html>"
    
@app.route('/book')
def show_book():
    db.session.get(book)
    bookAuthor = book.autho
    bookPage = book.page_count
    return render_template("book.html", author=bookAuthor, page=bookPage)