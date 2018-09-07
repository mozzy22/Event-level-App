import datetime
from db_conn import DbConn

class User:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age  = 0
        self.email =""
        self.password = ""
        self.created_at = None
        self.conn = DbConn()



    def add_user(self, first_name, last_name, age, email, password):
        conn = self.conn.create_connection()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at =  datetime.date.today()

        cur = conn.cursor()

        sql = """INSERT INTO Users ( first_name, last_name, age,email, password, created_at )
              VALUES ('{f_name}', '{l_name}', '{age}', '{email}', '{password}', '{created_at}' )"""

        sql_command = sql.format( f_name = self.first_name , l_name = self.last_name, age = self.age
                            , email =self.email, password = self.password, created_at = self.created_at)
        cur.execute(sql_command)
        conn.commit()
        conn.close()





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

if __name__ == "__main__":
    user = User()
    user.add_user("dd" ,"b" ,22, "email", "333")
