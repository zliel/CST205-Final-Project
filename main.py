import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

# read the dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    return {'message': 'Hello, World!'}
