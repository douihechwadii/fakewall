from action import Action

class SendAction(Action):
    def __init__(self, date, time, vd, eventtime, duration, packet, sentbyte, sentpkt, proto, action, trandisp, transip, transport):
        super().__init__(date, time, vd, eventtime, duration, packet)
        self.sentbyte = sentbyte
        self.sentpkt = sentpkt
        self.proto = proto
        self.action = action # The Action Type
        self.trandisp = trandisp
        self.transip = transip
        self.transport = transport


    def send(self, packet):
        return super().send(packet)