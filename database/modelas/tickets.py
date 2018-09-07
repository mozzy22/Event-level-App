
class Ticket():
    "A class to Manipulate tickets"

    def __init__(self):
        self.user_id = 0
        self.event_id =0
        self.is_valid = True
        self.varification_code = None
        self.created_at = None


    def add_ticket(self, user_id, event_id, bol ):
        self.user_id = user_id
        self.event_id = event_id
        self.event_id =bol

    def update_ticket(self, user_id, event_id, bol):
        self.user_id = user_id
        self.event_id = event_id
        self.event_id = bol

    def get_ticket(self,user_id,event_id ):
        self.user_id = user_id
        self.event_id =event_id

        return Ticket()


