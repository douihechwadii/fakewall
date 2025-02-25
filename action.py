class Action:
    def __init__(self, date, time, vd, eventtime, duration, packet):
        self.date = date
        self.time = time
        self.vd = vd
        self.eventtime = eventtime
        self.duration = duration
        self.packet = packet


    def send(self, packet):
        pass

    def receive(self, packet):
        pass