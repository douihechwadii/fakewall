class Actor:
    def __init__(self, ip, name, port, intf, intfrole, country, action):
        self.ip = ip
        self.name = name
        self.port = port
        self.intf = intf
        self.intfrole = intfrole
        self.country = country
        self.action = action # Action object

    def start(self, action):
        pass

    def stop(self, action):
        pass

    def accept(self, action):
        pass

    def refuse(self, action):
        pass