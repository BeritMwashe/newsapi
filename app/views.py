from flask import Flask, render_template
from .request import get_sources
from app import app




@app.route('/')
def index():
    sources=get_sources()
    return render_template('index.html',source=sources)