# Flask
from flask import (
    Flask,
    request,
    Response,
    render_template
)
from flask.app import Flask as FlaskApp

# Local
from models.book import Book

# faker
from faker import Faker

# random
import random as rd


fake = Faker()
app: FlaskApp = Flask(__name__)
books: list[Book] = []

@app.route("/<id>")
def book_page(id: str):
    return render_template(
        'book.html',
        book=books[int(id)]
    )

@app.route("/")
def main_page():
    return render_template(
        'index.html',
        books=enumerate(books)
    )

if __name__ == '__main__':
    _: int
    for _ in range(1000):
        book = Book(
            fake.name(),
            fake.text(),
            rd.randint(100, 600),
            round(
                rd.random() * 500 +
                rd.randint(1000, 10000),
                2
            ),
            [
                rd.randint(1, 5) 
                for _ in range(rd.randint(2, 6))
            ]
        )
        books.append(
            book
        )
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
