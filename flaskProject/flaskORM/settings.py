import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#
# SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite") #数据库地址 sqllite
#
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True #请求结束后自动提交
# SQLALCHEMY_RTACK_MODIFICATIONS = True #flask1版本之后，添加的选项，目的是跟踪修改
#
# DEBUG = True

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite") #数据库地址 sqllite
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #请求结束后自动提交
    SQLALCHEMY_RTACK_MODIFICATIONS = True #flask1版本之后，添加的选项，目的是跟踪修改

class RunConfig(Config):
    DEBUG = False
