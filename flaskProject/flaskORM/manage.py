from models import models
from views import app
from flask_script import Manager
manage = Manager(app)

@manage.command
def hello():
    print("hello")

@manage.command
def migrate():
    models.create_all()

if __name__ == "__main__":
    manage.run()

