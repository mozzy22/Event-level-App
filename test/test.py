import unittest
from registration.regester import Register

class Resgister_test(unittest.TestCase):
    def setUp(self):
        self.register = Register()

    def test_Registration_creation(self):
        self.assertIsInstance(self.register, Register)

    def test_invalid_email(self):
        invalid_email = self.register.validate_email("mozzymutesa")
        self.assertFalse(invalid_email)

    def test_valid_email (self):
        valid_email1 = self.register.validate_email("mozzymutesa@gmail.com")
        valid_email12 = self.register.validate_email("mozzymutesa@yahoo.com")
        self.assertTrue(valid_email1)
        self.assertTrue(valid_email12)

    def test_empty_invalid_email(self):
        empty_email = self.register.validate_email("")
        self.assertFalse(empty_email)

    def test_validate_empty_names(self):
        first_name = ""
        second_name =""
        valid = self.register.validate_empty_names(first_name, second_name)
        self.assertFalse(valid)

    def test_validate_names (self):
        first_name = "moses"
        second_name = "mutesasira"
        valid = self.register.validate_empty_names(first_name, second_name)
        self.assertTrue(valid)

    def test_vald_details_added(self):
        first_name = "moses"
        second_name = "mutesasira"
        email = "mozzymutesa@gmail.com"

        new_guest_details = {
            "id" :0 ,
            "first_name": first_name,
            "second_name": second_name,
            "email": email }

        self.register.register_guest(first_name, second_name, email)
        self.assertEqual(str(new_guest_details), str(self.register.guest_details))

    def test_invald_details_Not_added(self):
        first_name = "moses"
        second_name = "mutesasira"
        email = "mozzymutesa"

        self.register.register_guest(first_name, second_name, email)
        print("yaaa" + str(self.register.guest_details))
        self.assertEqual( str(self.register.guest_details), "{}")

    def test_Empty_details_Not_added(self):
        first_name = ""
        second_name = "mutesasira"
        email = "mozzymutesa"

        self.register.register_guest(first_name, second_name, email)
        print("yaaa" + str(self.register.guest_details))
        self.assertEqual( str(self.register.guest_details), "{}")


