from actor import Actor

class DestinationActor(Actor):
    def __init__(self, ip, name, port, intf, intfrole, country, action):
        super().__init__(ip, name, port, intf, intfrole, country, action)


    def accept(self, action):
        return super().accept(action)
    
    def refuse(self, action):
        return super().refuse(action)