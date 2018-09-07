from db_conn import Db_conn

class Event:
    "A class to describe the model event"

    def __init__(self):
        self.event_name = ""
        self.price = ""
        self.location  = ""
        self.conn = Db_conn()

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





    def update_event(self, event_name, price, location):
        self.event_name = event_name
        self.price = price
        self.location = location

    def get_event(self, event_name):
        self.event_name =event_name
        return Event()

if __name__ == "__main__":
    event = Event()
    event.add_event("prom", 3000, "luweero")