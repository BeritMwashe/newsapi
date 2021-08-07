from flask import Flask, render_template
from .request import get_Articles, get_sources
from app import app




@app.route('/')
def index():
    sources=get_sources()
    articles=get_Articles(category='everything',query='food')
    return render_template('articles.html',articles=articles)
    # return render_template('index.html',source=sources)