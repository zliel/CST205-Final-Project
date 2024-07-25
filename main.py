"""
Authors: Zackary Liel, Maria Santiago, Oscar Alvarado, and Smirth Luciano
Class: CST 205
Date: 7/24/2024
Abstract: This program is a web application that allows users to search for books based on a search query they enter.
The user can then select a book from the list and will be shown recommendations based on the chosen book. The user can then select a recommended book and will be shown information on the book such as the title, book cover, isbn, author's name, and the book's average rating.

Who did what:
- Zackary worked on the flask routes for the index and book_search_results, and the book_info route. He also worked on
the HTML templates for the index, book_search_results, and the template for book_search_results.html. He also worked on the README file.
- Maria finished the index's flask route and made its template. She also did the docstrings for the route functions.
- Oscar worked on the flask route and template for the recommendation_results route.
- Smirth worked on the flask route and template for the book_info route.
"""
import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

# read the dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
BIG_BOOK_BASE_URL = 'https://api.bigbookapi.com'


class Query(FlaskForm):
    query = StringField(
        'Query',
        validators=[DataRequired()]
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    """This route is for the initial search for a book recommendation"""
    form = Query()
    if form.validate_on_submit():
        return redirect(f'/book_search_results/{form.query.data}')
    return render_template('index.html', form=form)


@app.route('/book_search_results/<query>')
def book_search_results(query):
    """This route takes the user to the list of book recommendations based on the search query they entered"""
    response = requests.get(f'{BIG_BOOK_BASE_URL}/search-books?api-key={API_KEY}&query={query}&number=20')
    data = response.json()
    books = data.get('books', [])
    # print(f"Books: {books}")
    book_list = [
        {
            "id": book[0]["id"],
            "title": book[0]["title"],
            "subtitle": book[0].get("subtitle", ""),
            "cover_image_url": book[0]["image"]
        }
        for book in books
    ]
    return render_template('book_search_results.html', book_list=book_list, original_query=query)


@app.route('/recommendation_results/<int:book_id>', methods=['GET'])
def recommendation_results(book_id):
    """This route takes the user to another list of book recommendations based on the book recommendation they chose from the first list."""
    endpoint = f'https://api.bigbookapi.com/{book_id}/similar?api-key={API_KEY}'
    response = requests.get(endpoint)
    # print(f"Recommendations Response JSON: {response.json()}")
    books = response.json().get('similar_books', [])
    original_book_endpoint = f'https://api.bigbookapi.com/{book_id}?api-key={API_KEY}'
    orignal_response = requests.get(original_book_endpoint)
    original_book = orignal_response.json()
    book_list = [
        {
            "id": book["id"],
            "title": book["title"],
            "subtitle": book.get("subtitle", ""),
            "cover_image_url": book["image"]
        }
        for book in books
    ]
    # print(f"Book List: {book_list}")
    return render_template('recommendation_results.html', book_list=book_list,original_book_title=original_book['title'])


@app.route('/book_info/<int:book_id>', methods=['GET'])
def book_info(book_id):
    """This route provides the user with the information on the book they selected such as title, book image, isbn, author's name and the books average rating."""
    endpoint = f'https://api.bigbookapi.com/{book_id}?api-key={API_KEY}'
    response = requests.get(endpoint)
    book = response.json()
    # print(f'raw:{book}')
    book_info = {
        "title": book.get("title"),
        "cover_image_url": book.get("image"),
        "isbn": book.get("identifiers", {}).get("isbn_10"),
        "author_name": ", ".join(author.get("name") for author in book.get("authors", [])),  # Getting all author names
        "average_rating": book.get("rating", {}).get("average"),
    }
    # print (f"book info{book_info}")
    return render_template('book_info.html', book_info=book_info)


if __name__ == '__main__':
    app.run(debug=True)
