import base64
from flask_testing import TestCase
from app import *
import unittest
import json

def logout_teacher():
    pass

class TestTeacher(TestCase):
    data = {
        "username": "nadiia3",
      "password": "3333",
      "first_name": "nadiia3",
      "last_name": "Zykova"
    }

    tester = app.test_client()

    s = '{}:{}'.format(data['username'], data['password'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic ' + base64.b64encode(s.encode()).decode()}

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def create_teacher(self, data=None):
        if data is None:
            data = self.data
        username = data.get('username', None)
        password = data.get('password', None)
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        if username and password and first_name and last_name:
            response = self.tester.post("/teacher", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(200, response.status_code)
        if Teacher.query.filter_by(username=username).first() is not None:
            response = self.tester.post("/teacher", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(400, response.status_code)
        else:
            response = self.tester.post("/teacher", data=json.dumps(data), content_type='application/json')
            return self.assertEqual(204, response.status_code)

    def test_post_teacher(self):
        self.create_teacher()

    def test_get_teachers(self):
        self.create_teacher()
        self.create_teacher()
        self.create_teacher()
        response = self.tester.get("/teacher", content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_missing_json_login(self):
        self.create_teacher()
        response = self.tester.get("/teacher/login", content_type='application/json')
        return self.assertEqual(400, response.status_code)

    def test_login(self):
        self.create_teacher()
        response = self.tester.get("/teacher/login", data=json.dumps(self.data),
                                   headers=self.headers, content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_unauthorized_logout(self):
        response = self.tester.get('/teacher/logout')
        statuscode = response.status_code
        self.assertEqual(401, statuscode)

    def test_logout(self):
        logout_teacher()

    def test_delete_teacher(self):
        self.create_teacher()
        response = self.tester.delete('/teacher/1', headers=self.headers)
        return self.assertEqual(201, response.status_code)

    def test_delete_teacher_not_found(self):
        self.create_teacher()
        response = self.tester.delete("/teacher/", data=json.dumps(self.data),
                                   headers=self.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()