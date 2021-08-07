from app.config import DevConfig
from flask import Flask


app=Flask(__name__)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
from app import views