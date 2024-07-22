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
    return {'message': f'You searched for: {query}'}
