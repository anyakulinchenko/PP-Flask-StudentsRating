from migrate import db

Base = db.Model


class Student(db.Model):
    __tablename__ = 'students'
    sid = db.Column('sid', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.VARCHAR(length=30))
    last_name = db.Column('last_name', db.VARCHAR(length=40))
    total_rating = db.Column('total_rating', db.Integer)


class Rating(db.Model):
    __tablename__ = 'ratings'
    rid = db.Column('rid', db.Integer, primary_key=True)
    subject = db.Column('subject', db.VARCHAR(length=30))
    svalue = db.Column('svalue', db.Integer)
    sid = db.Column(db.Integer, db.ForeignKey(Student.sid))
    tmp = db.relationship('Student')


class Teacher(db.Model):
    __tablename__ = 'teachers'
    tid = db.Column('tid', db.Integer, primary_key=True)
    username = db.Column('username', db.VARCHAR(length=40), nullable=False)
    password = db.Column('password', db.VARCHAR(length=40), nullable=False)
    first_name = db.Column('first_name', db.VARCHAR(length=30))
    last_name = db.Column('last_name', db.VARCHAR(length=40))


