from flask import Flask, render_template
from .request import get_Articles, get_sources
from app import app




@app.route('/')
def index():
    sos=get_sources()
    sourcePassed=''
    articles=get_Articles(category='everything',query='all')
    
    return render_template('index.html',source=sos,sourcePassed=sourcePassed,articles=articles
    )


@app.route('/articles/<source>')
def articles(source):
    
    articles=get_Articles(category='everything',query='all')
    source=source[2:-3]
    return render_template('articles.html',articles=articles,source=source)
@app.route('/top-headlines')
def headlines():
   
    articles=get_Articles(category='top-headlines',query='politics')
    source=''
    # return render_template('articles.html',articles=articles)
    return render_template('articles.html',articles=articles,source=source)

@app.route('/articles')
def article_link():
    
    articles=get_Articles(category='everything',query='all')
    source=''
    return render_template('articles.html',articles=articles,source=source)