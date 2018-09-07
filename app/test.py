import unittest
import json
from users_model import Users
from routes import My_app

class Test_Case(unittest.TestCase):

    def setUp(self):
        " setting p variables to run before test"
        self.user_obj = Users()
        self.hostname = "http://localhost:5000/api/"
        self.app = My_app.test_client()
        self.app.testing = True
        self.user = {
	             "user_name" : "Mutesasira",
                 "user_pasword" : "bb",
                 "user_location": "cc",
                 "user_age" :26
                    }


    def test_wrong_get_method(self):
        "asserting a wrong method for get"
        res = self.app.post(self.hostname + "get-users", data=self.user)
        self.assertEqual(res.status_code, 405)

    def test_right_get_method(self):
        "asserting a correct method"
        res = self.app.get(self.hostname + "get-users")
        self.assertEqual(res.status_code, 200)

    def test_wrong_post_method(self):
        " asserting a wrong method foor post"
        resp = self.app.get(self.hostname + "add-user", data=self.user)
        self.assertEquals(resp.status_code, 405)

    def test_rigt_method(self):
        "asserting a right method for post"
        resp = self.app.post(self.hostname + "add-user", data=self.user)
        self.assertEquals (resp.status_code ,200)

    def test_wrong_delete_method(self):
        "asserting a wrong delete method"
        res = self.app.post(self.hostname + "delete/dd", data=self.user)
        self.assertEqual(res.status_code, 405)

    def test_right_delete_method(self):
        "asserting a correct delete method"
        res = self.app.delete(self.hostname + "delete/dd")
        self.assertEqual(res.status_code, 200)

    def test_empty_user_list(self):
        "asserting user list is empty before any post"
        resp = self.app.get(self.hostname + "get-users")
        self.assertEqual(len(self.user_obj.users_list), 0)

    def test__user_added_to_list(self):
        "asserting a user added after a correct pst method"
        resp = self.app.post(self.hostname + "add-user", data = json.dumps(self.user ),content_type='application/json',)
        #resp = self.app.get(self.hostname + "get-users")
        self.assertIn(self.user['user_name'], str(resp.data))

