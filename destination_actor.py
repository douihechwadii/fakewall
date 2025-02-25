from actor import Actor

class DestinationActor(Actor):
    def __init__(self, ip, name, port, intf, intfrole, country, action):
        super().__init__(ip, name, port, intf, intfrole, country, action)