from models import *

student = Student(first_name='Anna', last_name='Kulincenko', total_rating=0)
teacher = Teacher(username='tusername', password='tpassword', first_name='Nadiia', last_name='Zykova')
rating1 = Rating(subject='math', svalue=5, sid=1, tmp=student)
rating2 = Rating(subject='math', svalue=3, sid=1)
student1 = Student(first_name='Vfef', last_name='bb', total_rating=0)
student2 = Student(first_name='ccc', last_name='cco', total_rating=0)
#db.create_all()

db.session.add(student)
db.session.add(student1)
db.session.add(student2)
db.session.add(teacher)
db.session.add(rating1)
db.session.add(rating2)
db.session.commit()
