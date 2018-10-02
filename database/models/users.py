import datetime
from db_conn import DbConn

class User:
    "A user class to manage user data"

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age  = 0
        self.email =""
        self.password = ""
        self.user_id = 0
        self.created_at = None
        self.conn = DbConn()

    def add_user(self, first_name, last_name, age, email, password):
        "A function to add user to data base"
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
        "A function to update a user"
        conn = self.conn.create_connection()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at = datetime.date.today()
        cur = conn.cursor()

        sql = """UPDATE Users  SET last_name = '{l_name}' ,age = '{age}', email = '{email}', 
                 password = '{pass1}', created_at ='{date}'  WHERE first_name = '{f_name}' ;"""

        sql_command = sql.format( f_name = self.first_name , l_name = self.last_name, age = self.age
                            , email =self.email, pass1 = self.password, date = self.created_at)

        cur.execute(sql_command)
        conn.commit()
        conn.close()




    def get_user(self, first_name):
         conn = self.conn.create_connection()
         self.first_name = first_name
         cur = conn.cursor()

         sql =  """SELECT * FROM Users WHERE first_name = '{f_name}' ;"""
         sql_command = sql.format(f_name = self.first_name)

         cur.execute(sql_command)
         rows = cur.fetchall()
         user = {}
         for row in rows:
             user = {
             "user_d" : row[0],
             " first_name" : row[1] ,
             "last_name" : row[2],
             " age " : row[3],
             " email": row[4],
             " password": row[5],
                 "date_created": row[6],
                 }
         conn.commit()
         conn.close()
         #return User()
         print(user)

    def get_user_event(self, user_id):

        conn = self.conn.create_connection()
        self.user_id =user_id
        cur = conn.cursor()

        sql = """SELECT * FROM Tcket WHERE user_id = '{u_id}' ;"""
        sql_command = sql.format(u_id=self.user_id)

        cur.execute(sql_command)
        rows = cur.fetchall()
        user = {}
        for row in rows:
            user = {
                "ticket_id": row[0],
                " user_id": row[1],
                "event_id": row[2],
                "is_valid": row[3],
                " verification_code": row[4],
                " date_created": row[5],

            }


        conn.commit()
        conn.close()
        # return User()
        print(user)



if __name__ == "__main__":
    user = User()
    #user.add_user("mutesa" ,"moese" ,22, "email", "333")
    #user.update_user("mutesa", "moefjfjfjfse", 2233, "emailupdated", "333update")
    #user.get_user("dd")
    user.get_user_event(1)
