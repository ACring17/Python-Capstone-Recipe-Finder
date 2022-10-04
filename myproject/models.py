#Where the models will be housed
from myproject import db 

class Recipes(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    name = db.Column(db.Text)

    def __init__(self,username,password,name):
        self.username = username
        self.password = password
        self.name = name
    # String represenation of the db
    def __repr__(self):
        return f"Welcome {self.name} to Recipe Finder"
