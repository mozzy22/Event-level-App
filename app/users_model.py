import uuid
class Users :
    "Model class for users"

    def __init__(self):
        "Decalring class member"
        self.users_list = []
        self.user_details = {}
        self.user_id = ""
        self.user_name = ""
        self.user_pasword = ""
        self.user_location = ""
        self.user_age=  ""

    def add_user(self,user_name, user_pasword, user_location, user_age):
        "A function to add a user"
        self.user_id = str(uuid.uuid1())
        self.user_name = user_name
        self.user_pasword = user_pasword
        self.user_location =user_location
        self.user_age= user_age
        self.user_details = {
                "user_id" : self.user_id ,
                "user_name" : self.user_name,
                "user_pasword" : self.user_pasword,
                 "user_location": self.user_location,
                 "user_age" : self.user_age
                 }
        self.users_list.append(self.user_details )




    def validate_user_obj (self, user_Obj):
        "A function to validate a user object"
        if ("user_name" in user_Obj and "user_pasword" in user_Obj
            and "user_location" in user_Obj and "user_age" in user_Obj):
            return True
        else:
            return False


    def return_users (self):
        "a Function to return all user"
        return self.users_list

    def delete_user(self, user):
        "A function to delete a user from the List"
        self.users_list.remove(user)





