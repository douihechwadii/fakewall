from actor import Actor

class SourceActor(Actor):
    def __init__(self, ip, name, port, intf, intfrole, country, action, mac, mastermac, server):
        super().__init__(ip, name, port, intf, intfrole, country, action)
        self.mac = mac
        self.mastermac = mastermac
        self.server = server


    def start(self, action):
        return super().start(action)
    
    def stop(self, action):
        return super().stop(action)


