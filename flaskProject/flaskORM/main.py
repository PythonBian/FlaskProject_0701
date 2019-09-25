import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config") #来源于类对象
app.secret_key = "123123"
models = SQLAlchemy(app)
