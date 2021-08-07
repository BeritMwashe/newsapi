from app.config import DevConfig
from flask import Flask


app=Flask(__name__)

app.config.from_object(DevConfig)
from app import views