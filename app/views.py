from flask import Flask, render_template
from .request import get_Articles, get_sources
from app import app




@app.route('/')
def index():
    sources=get_sources()
   
    
    return render_template('index.html',source=sources)


@app.route('/articles')
def articles():
    
    articles=get_Articles(category='everything',query='food')
    # return render_template('articles.html',articles=articles)
    return render_template('articles.html',articles=articles)
@app.route('/top-headlines')
def headlines():
   
    articles=get_Articles(category='top-headlines',query='politics')
    # return render_template('articles.html',articles=articles)
    return render_template('articles.html',articles=articles)