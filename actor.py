from random import *

class Actor:
    def __init__(self, ip, name, port, intf, action):
        self.ip = ip
        self.name = name
        self.port = port
        self.intf = intf
        self.action = action # an action object 
        self.intfrole = "Undefined"
        self.country = "Reserved"


    # for wanting to defines the properties randomly
    def ip_init(self):
        self.ip = "192.168." + randint(0, 255) + "." + random(0, 255)
    
    def port_init(self):
        self.port = randint(1000, 9999)

    def intf_init(self):
        self.intf = "port" + random(1,99)
    
    def __str__(self):
        return f"Actor: {self.ip}, {self.name}, {self.port}, {self.intf}, {self.intfrole}, {self.country}"