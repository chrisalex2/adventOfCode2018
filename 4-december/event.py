class Event(object):
    date_time = ""
    description = ""
    guard = ""

    def __init__(self, date_time, description):
        self.date_time = date_time
        self.description = description

    def __str__(self):
        return "Date Time: " + self.date_time + "\nDescription: " + self.description
