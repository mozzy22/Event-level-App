from user import User


class GuestList():
    " A class to handle deleting, adding and retrieving of users"

    def __init__ (self):
        self.user_obj = User ("mutesa","mutesa@gmail","uganndan","luweero",30)
        self.user_list = []
        self.user_list.append(self.user_obj.get_user_details())


    def add_user(self, name, email, nationality, village , age):
        "A functon to add a user"

        self.user_obj.add_user_details(name, email, nationality, village , age)

        if name and email and "@" in email:
            self.user_list.append(self.user_obj.get_user_details())
            return self.user_list

        else:
            return "Invaid / null user details"  + "\n ............"

    def delete_user(self, name):
        "A function to delete user"
        del_user = {}
        for user in self.user_list:
            if user["name"] == name:
                del_user = user
                self.user_list.remove(user)
            else:
                pass

        if del_user:
            return("succesfuly deleted  " + str(del_user) + "\n Remaining list" + str(self.user_list)+ "\n ............")
        else :
            return("specified use name doesnt exist, no user deleted")



    def get_user(self, name):
        "A function to get a user"
        get_user = {}

        for user in self.user_list:
            if user["name"] == name:
                get_user = user
            else:
                pass

        if get_user:
            return str(get_user) + "\n ............"
        else :
            return "ERRO>>>> Specified user doent Exist !!!!!!!!!!"


    def get_all_users(self):
        "A function to get all users"
        if self.user_list:
            return str("all registred users ..........\n" + str(self.user_list) + "\n ............")
        else :
            return "User list empty"




if __name__ == "__main__":
    guest = GuestList()
   # print(guest.get_user(input("Enter name :")))
   # print(guest.get_all_users())
    #print(guest.user_obj.get_user_details())
    #print(guest.user_obj.get_person_details())
    print (guest.add_user("mozzy", "mozzymu@tesagmail", "Kenyan" ,"luweero", 20))
    print(guest.get_all_users())
   # print(guest.get_user(input("Enter name :")))
    print(guest.delete_user(input("Enter user to delete!! >>")))



