import unittest
import json
from users_model import Users
from routes import My_app

class Test_Case(unittest.TestCase):

    def setUp(self):
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
        res = self.app.post(self.hostname + "get-users", data=self.user)
        self.assertEqual(res.status_code, 405)

    def test_right_get_method(self):
        res = self.app.get(self.hostname + "get-users")
        self.assertEqual(res.status_code, 200)

    def test_wrong_post_method(self):
        resp = self.app.get(self.hostname + "add-user", data=self.user)
        self.assertEquals(resp.status_code, 405)

    def test_rigt_method(self):
        resp = self.app.post(self.hostname + "add-user", data=self.user)
        # self.assertEqual(len(self.user_obj.users_list), 1)
        self.assertEquals (resp.status_code ,200)

    def test_wrong_delete_method(self):
        res = self.app.post(self.hostname + "delete/dd", data=self.user)
        self.assertEqual(res.status_code, 405)

    def test_right_delete_method(self):
        res = self.app.delete(self.hostname + "delete/dd")
        self.assertEqual(res.status_code, 200)

    def test_empty_user_list(self):
        resp = self.app.get(self.hostname + "get-users")
        self.assertEqual(len(self.user_obj.users_list), 0)

    def test__user_added_to_list(self):
        resp = self.app.post(self.hostname + "add-user", data = json.dumps(self.user ),content_type='application/json',)
        #resp = self.app.get(self.hostname + "get-users")
        self.assertIn(self.user['user_name'], str(resp.data))

