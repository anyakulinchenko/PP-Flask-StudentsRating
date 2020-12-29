from werkzeug.security import check_password_hash
from config import *
from models import *


@app.route('/teacher', methods=['POST'])
def create_teacher():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    first_name = request.json.get('first_name', None)
    last_name = request.json.get('last_name', None)
    teacher = Teacher(username=username, password=password, first_name=first_name, last_name=last_name)
    db.session.add(teacher)
    db.session.commit()
    return jsonify({"Success": "Teacher has been created"}), 200

@app.route('/teacher', methods=['GET'])
def get_teachers():
    teacher = Teacher.query.all()
    teacher_list = {'teacher_list': []}
    for i in teacher:
        teacher_list['teacher_list'].append({'username': i.username, 'password': i.password, 'fist_name': i.first_name, 'last_name': i.last_name})
    return jsonify(teacher_list)

@app.route('/teacher/login', methods=['GET'])
def teacher_login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    current_teacher = Teacher.query.filter_by(username=username)
    for i in current_teacher:
        if check_password_hash(i.password, password):
            return jsonify({"login status": "success"}), 200
    else:
        return jsonify({"Error": "Wrong password"}), 401


@app.route('/teacher/logout', methods=['GET'])
@auth.login_required
def teacher_logout():
    return jsonify({"message": "success"}), 200


@app.route('/teacher/<tid>', methods=['DELETE'])
@auth.login_required
def delete_teacher(tid):
    teacher = Teacher.query.get(tid)
    if teacher is None:
        return jsonify(status='Teacher not found'), 404
    db.session.delete(teacher)
    db.session.commit()
    return jsonify(status='deleted'), 201