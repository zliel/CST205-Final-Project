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
    form = Query()
    if form.validate_on_submit():
        return redirect(f'/book_search_results/{form.query.data}')
    return {'message': 'Hello, World!'}
    # return render_template('index.html', form=form)


@app.route('/book_search_results/<query>')
def book_search_results(query):
    response = requests.get(f'{BIG_BOOK_BASE_URL}/search-books?api-key={API_KEY}&query={query}&number=20')
    data = response.json()
    return {'book_list': data['books']}
    # return render_template('book_search_results.html', book_list=data['books'])
