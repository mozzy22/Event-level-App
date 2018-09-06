
from person import Person

class User(Person):

    def __init__(self, name, email, nationality, village , age):
        super().__init__(nationality, village , age)
        self.name = name
        self. email = email
        self.user_details ={}

    def add_user_details(self, name, email, nationality, village , age):
        self.name = name
        self.email = email
        self.nationality = nationality
        self.village = village
        self.age = age



    def get_user_details (self):

        self.user_details = {
                "name" : self.name,
                "email": self.email,
                "nationality": self.nationality,
                "village": self.village,
                "age": self.age,
                }

        return(self.user_details )


if __name__ == "__main__":
    user = User("mozzy", "mozzymutesagmail", "Kenyan" ,"luweero", 20)
    print(user.get_person_details())
    print (user.get_user_details())