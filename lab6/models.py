from migrate import db

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
    username = db.Column('username', db.VARCHAR(length=40), nullable=False)
    password = db.Column('password', db.VARCHAR(length=40), nullable=False)
    first_name = db.Column('first_name', db.VARCHAR(length=30))
    last_name = db.Column('last_name', db.VARCHAR(length=40))


