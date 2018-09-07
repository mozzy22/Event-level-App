import psycopg2

class Db_conn :

    def create_connection(self):
        "A function to set up database connection"
        self.conn = psycopg2.connect(database = "Events_Db", user = "moses", password = "moses", host = "127.0.0.1", port = "5432")
        return self.conn



    def create_users_table(self):
        "A function to create the users_table"
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Users
              (user_id  SERIAL PRIMARY KEY  NOT NULL  ,
              first_name   TEXT   NOT NULL,
              last_name  TEXT NOT NULL,
               age     TEXT NOT NULL,
               email     TEXT NOT NULL ,
               password   TEXT NOT NULL,
               created_at  DATE  ); ''')
        print("Table users created successfully")


    def create_events_table(self):
        "A function to create the users_table"
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Event
                     (event_id  SERIAL PRIMARY KEY    NOT NULL ,
                      event_name    TEXT    NOT NULL,
                      price  MONEY NOT NULL,
                      location   TEXT NOT NULL ); ''')
        print("Table events created successfully")



    def create_ticket_table(self):
        "A function to create the ticket table"
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Tcket
                           (ticket_id  SERIAL PRIMARY KEY   NOT NULL ,
                            user_id    INT    references Users(user_id) NOT NULL,
                            event_id   INT     references Event(event_id) NOT NULL,
                            is_valid   BOOLEAN , 
                            verification_code   UUID NOT NULL ,
                            created_at  DATE  ); ''')
        print("Table ticket created successfully")


    def close_DB(self):
        self.conn.commit()
        self.conn.close()



# if __name__ == '__main__':
#         db = Db_conn()
#         db.create_connection()
# #       db.create_users_table()
# #       db.create_events_table()
#         db.create_ticket_table()
#         db.close_DB()