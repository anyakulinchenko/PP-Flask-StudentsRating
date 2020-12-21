from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from config import *
from models import *



@app.route('/student', methods=['POST'])
def post_student():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    total_rating = request.json.get('total_rating', None)
    student = Student(first_name=first_name, last_name=last_name, total_rating=total_rating)
    db.session.add(student)
    db.session.commit()
    return jsonify({"msg": "Student successfully added"}), 200


@app.route('/student', methods=['GET'])
def get_students():
    student = Student.query.order_by(Student.total_rating.desc()).all()
    student_list = {'student_list': []}
    for i in student:
        student_list['student_list'].append({'total_rating': i.total_rating, 'fist_name': i.first_name, 'last_name': i.last_name})
    return jsonify(student_list)


@app.route('/student/<sid>', methods=['PUT'])
def put_student(sid):
    student = Student.query.get(sid)
    if student is None:
        return jsonify(status='student not found'), 404
    student.total_rating = request.json.get('total_rating', None)
    if student.total_rating:
        db.session.commit()
        return jsonify(status='update student'), 202
    else:
        return jsonify(status='Bad input data'), 204


@app.route('/student/<sid>', methods=['DELETE'])
def delete_student(sid):
    student = Student.query.get(sid)
    if student is None:
        return jsonify(status='student not found'), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify(status='deleted'), 200


