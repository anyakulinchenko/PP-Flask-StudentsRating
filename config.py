from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root',
    password='1111',
    server='localhost',
    database='mydb'
)

db = SQLAlchemy(app)
engine = db.engine
Base = db.Model

from werkzeug.security import check_password_hash
from models import *
@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    teacher = Teacher.query.filter_by(username=username).first()
    if teacher is None:
        return False
    else:
        return check_password_hash(teacher.password, password)
