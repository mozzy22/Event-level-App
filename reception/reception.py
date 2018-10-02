

class Register_checker():
    "A class to check whther the vistor is registred or not"
    ordinary_file = open("ordinary_list.txt" , "r")
    vip_file = open("vip_list.txt" , "r")

    ordinary_list = []
    vip_list =[]
    payed_List = []

  #checking whether a vistor is registred or not
    def registration_checker(self, vistor):
        with self.ordinary_file as ordinary_names:
            self.ordinary_list = ordinary_names.readlines()
            self.ordinary_file.close()

        with self.vip_file as vip_names:
            self.vip_list = vip_names.readlines()
            self.vip_file.close()

        for name in self.ordinary_list:
            if vistor.lower() in name.lower():
                print(name.strip('\n')  + ", ORDINARY")
                self.payed_List.append(vistor)
            else:
                pass

        for name in self.vip_list:
            if vistor.lower() in name.lower():
                print(name.strip('\n') + ", VIP")
                self.payed_List.append(vistor)
            else:
                pass

        if  vistor not in self.payed_List :
            print( vistor + " Not Registered!!!!")








if __name__ == '__main__':
    x = Register_checker()
    vistor = input("enter vistor's name :")
    x.registration_checker(vistor)