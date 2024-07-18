from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)


@app.route('/')
def index():
    return {'message': 'Hello, World!'}
