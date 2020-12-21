from migrate import db
from werkzeug.security import generate_password_hash

Base = db.Model


class Student(db.Model):
    __tablename__ = 'students'
    sid = db.Column('sid', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.VARCHAR(length=30))
    last_name = db.Column('last_name', db.VARCHAR(length=40))
    total_rating = db.Column('total_rating', db.Integer)

class Teacher(db.Model):
    __tablename__ = 'teachers'
    tid = db.Column('tid', db.Integer, primary_key=True)
    username = db.Column('username', db.VARCHAR(length=30), nullable=False)
    password = db.Column('password', db.VARCHAR(length=128), nullable=False)
    first_name = db.Column('first_name', db.VARCHAR(length=30))
    last_name = db.Column('last_name', db.VARCHAR(length=40))

    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = generate_password_hash(password)
        self.first_name = first_name
        self.last_name = last_name



