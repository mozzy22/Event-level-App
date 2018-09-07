import uuid
import datetime
from db_conn import Db_conn

class Ticket():
    "A class to Manipulate tickets"

    def __init__(self):
        self.user_id = 0
        self.event_id =0
        self.is_valid = True
        self.varification_code = None
        self.created_at = None
        self.conn = Db_conn()


    def add_ticket(self, user_id, event_id, is_valid ):
        conn = self.conn.create_connection()
        self.user_id = user_id
        self.event_id = event_id
        self.is_valid = is_valid
        self.varification_code = uuid.uuid1()
        self.created_at = datetime.date.today()


        cur = conn.cursor()

        sql = """INSERT INTO Tcket ( user_id ,event_id, is_valid,verification_code, created_at   )
                      VALUES ('{user_id}', '{event_id}', '{is_valid}', '{ver_code}', '{created_at}')"""

        sql_command = sql.format(user_id = self.user_id, event_id=self.event_id, is_valid =self.is_valid
                                 , ver_code =self.varification_code,  created_at=self.created_at)
        cur.execute(sql_command)
        conn.commit()
        conn.close()




    def update_ticket(self, user_id, event_id, bol):
        self.user_id = user_id
        self.event_id = event_id
        self.event_id = bol

    def get_ticket(self,user_id,event_id ):
        self.user_id = user_id
        self.event_id =event_id

        return Ticket()


if __name__ == "__main__":
    ticket = Ticket()
    ticket.add_ticket(1,1,True)