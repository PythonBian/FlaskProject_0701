import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_pyfile("settings.py")
#app.config.from_envvar() #来源于环境变量，环境变量的值是python文件名称
#app.config.from_json() #来源于json文件,必须符合json格式
#app.config.from_mapping() #字典格式
app.config.from_object("settings.Config") #来源于类对象
#第一种，直接写配置文件
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite") #数据库地址 sqllite
#
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True #请求结束后自动提交
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True #flask1版本之后，添加的选项，目的是跟踪修改

models = SQLAlchemy(app)

