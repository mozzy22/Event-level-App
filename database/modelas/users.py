
class User:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age  = 0
        self.email =""
        self.password = ""
        self.created_at = None



    def add_user(self, first_name, last_name, age, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at = None

    def update_user(self, first_name, last_name, age, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at = None

    def get_user(self, first_name, last_name):
         self.first_name = first_name
         self.last_name = last_name

         return User()


