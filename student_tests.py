from teacher_tests import *

class TestStudent(TestCase):
    data = {
        "first_name": "first_name",
        "last_name": "last_name",
        "total_rating": 1
    }

    tester = app.test_client()
    teacher = TestTeacher()

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def create_student(self, data=None):
        if data is None:
            data = self.data
        self.teacher.create_teacher()
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        total_rating = data.get('total_rating', None)
        if first_name and last_name and total_rating:
            response = self.tester.post("/student", data=json.dumps(data),
                                        headers=self.teacher.headers,
                                        content_type='application/json')
            return self.assertEqual(200, response.status_code)
        else:
            response = self.tester.post("/articles", data=json.dumps(data),
                                        headers=self.teacher.headers,
                                        content_type='application/json')
            return self.assertEqual(400, response.status_code)

    def put_student(self):
        self.create_student()
        response = self.tester.put("/student/1", data=json.dumps(self.data),
                                   headers=self.teacher.headers,
                                   content_type='application/json')
        return self.assertEqual(202, response.status_code)

    def test_post_student(self):
        self.create_student()

    def test_unauthorized_401(self):
        response = self.tester.post('/student')
        statuscode = response.status_code
        self.assertEqual(401, statuscode)

    def test_get_students_success(self):
        self.create_student()
        self.create_student()
        self.create_student()
        self.create_student()
        response = self.tester.get("/student", content_type='application/json')
        return self.assertEqual(200, response.status_code)

    def test_put_student_success(self):
        return self.put_student()

    def test_put_student_bad_data(self):
        self.create_student()
        data = {
            "total": 1
        }
        response = self.tester.put("/student/1", data=json.dumps(data),
                                   headers=self.teacher.headers,
                                   content_type='application/json')
        return self.assertEqual(204, response.status_code)

    def test_put_student_not_found(self):
        self.teacher.create_teacher()
        response = self.tester.put("/student/1", data=json.dumps(self.data),
                                   headers=self.teacher.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)

    def test_delete_student_success(self):
        self.create_student()
        response = self.tester.delete('/student/1', headers=self.teacher.headers)
        return self.assertEqual(201, response.status_code)

    def test_delete_student_not_found(self):
        self.teacher.create_teacher()
        self.create_student()
        response = self.tester.delete("/student/", data=json.dumps(self.data),
                                   headers=self.teacher.headers,
                                   content_type='application/json')
        return self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()