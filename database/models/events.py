from db_conn import DbConn

class Event:
    "A class to describe the model event"

    def __init__(self):
        self.event_id = 0
        self.event_name = ""
        self.price = ""
        self.location  = ""
        self.conn = DbConn()

    def add_event(self,event_name, price, location):
        conn = self.conn.create_connection()
        self.event_name = event_name
        self.price =price
        self.location = location

        cur = conn.cursor()

        sql = """INSERT INTO Event ( event_name ,price, location)
                              VALUES ('{event_name}', '{price}', '{location}')"""

        sql_command = sql.format(event_name =self.event_name, price=self.price, location=self.location)
        cur.execute(sql_command)
        conn.commit()
        conn.close()





    def update_event(self,event_id, event_name, price, location):
        conn = self.conn.create_connection()
        self.event_id = event_id
        self.event_name = event_name
        self.price = price
        self.location = location
        cur = conn.cursor()

        sql = """UPDATE Event  SET event_name = '{e_name}' ,price = '{price}', location = '{location}'
                 WHERE event_id = '{id}';"""

        sql_command = sql.format(e_name=self.event_name, price =self.price, location=self.location , id = self.event_id)


        cur.execute(sql_command)
        conn.commit()
        conn.close()



    def get_event(self, event_name):
        conn = self.conn.create_connection()
        self.event_name =event_name
        cur = conn.cursor()
        sql = """SELECT * FROM Event WHERE event_name = '{e_name}' ;"""
        sql_command = sql.format(e_name = self.event_name)

        cur.execute(sql_command)
        rows = cur.fetchall()
        event = {}
        for row in rows:
            event = {
                "event_id": row[0],
                " event_name": row[1],
                "price": row[2],
                " location": row[3]

            }
        conn.commit()
        conn.close()

        print (event)

if __name__ == "__main__":
    event = Event()
    #event.add_event("prom", 3000, "luweero")
   # event.update_event(1,"promupdate", 3444000, "4444luweero")
    event.get_event("promupdate")