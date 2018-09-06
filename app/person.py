
__author__ = "Mutesasira Moses"

class Person:
    "A class to describe tge general attributesof a person"

    def __init__(self, nationality, village, age):
        self.nationality = nationality
        self.village = village
        self.age = age
        self.yesr_of_birth = 0

    def get_person_details(self):
        self.yesr_of_birth = 2018 - self.age
        return ".......... \n The Person is a {} , \n aged {} ,\n born in {} ,\n at {} \n ............."\
            .format(self.nationality, self.age, self.yesr_of_birth, self.village)


if __name__ == "__main__":
    p = Person("Ugandan", "kasana",30 )
    print(p.get_person_details())