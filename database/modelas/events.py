
class Event:
    "A class to describe the model event"

    def __init__(self):
        self.event_name = ""
        self.price = ""
        self.location  = ""

    def add_event(self,event_name, price, location):
        self.event_name = event_name
        self.price =price
        self.location = location

    def update_event(self, event_name, price, location):
        self.event_name = event_name
        self.price = price
        self.location = location

    def get_event(self, event_name):
        self.event_name =event_name
        return Event()
