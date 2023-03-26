class Booking:
    
    def __init__(self, date, time, treatment_list=None, id=None):
        self.date = date
        self.time = time
        self.treatment_list = treatment_list
        self.id = id
