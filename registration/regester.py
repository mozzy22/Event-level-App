import re
__author__ = "Mutesasira Moses"

class Register:
    "A class that registers guests for the event"

    def __init__(self):
        "Decalring class members"
        self.guest_list = []
        self.guest_details = dict()
        self.first_name = ""
        self.second_name = ""
        self.email = ""
        self.id = 0


    def read_file(self):
        # reading a file text to the list
        with open('regestry.txt', 'r') as old_list:
            self.guest_list = old_list.readlines()
            self.id = len(self.guest_list)
            old_list.close()

    def register_guest(self,first_name, second_name, email):
        "A function that takes user details and adds it to the list"

        if first_name and second_name:
            self.first_name = first_name
            self.second_name = second_name
            self.validate_email(email)

        else:
            print("Empty names , Please enter name!!!")

        if self.email:
            self.guest_details = {
                "id": self.id ,
                "first_name" : self.first_name,
                "second_name": self.second_name,
                "email": self.email  }
            self.guest_list.append(self.guest_details)
            print("new user details  >>" + str(self.guest_details))
        else:
            print ("ivalid/empty email, please Enter valid email !!!")


    def write_to_file(self):
        if self.guest_details:
            # writing the new user details to atext filr
            with open('regestry.txt', 'a') as guest_list:
                guest_list.write(str(self.guest_details) + "\n")
                guest_list.close()

    def print_current_list(self):
        with open('regestry.txt', 'r') as old_list:
            self.guest_list = old_list.readlines()
            self.id = len(self.guest_list)
            print("Current Guest List ..........")
            for detail in self.guest_list:
                print(detail.strip("\n"))
            old_list.close()
            print("\n .....................")

    def validate_email(self,email):
        "function to verify email"
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if match == None:
            return False
        else:
            self.email = email
            return True

    def clear_file_content(self):
        "A function to clear the text file"
        open('regestry.txt', "w").close()


if __name__ == "__main__":
    Reg = Register()
    first_name = input("Enter first name:")
    second_name = input("Enter second name:")
    email = input("Enter emal:")
    Reg.read_file()
    Reg.print_current_list()
    Reg.register_guest(first_name,second_name,email)
    Reg.write_to_file()

