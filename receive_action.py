from action import Action

class ReceiveAction(Action):
    def __init__(self, date, time, vd, eventtime, duration, rcvbyte, rcvpkt, poluuid, sessionid, policyid, policytype, policymode, service):
        super().__init__(date, time, vd, eventtime, duration)
        self.rcvbyte = rcvbyte
        self.rcvpkt = rcvpkt
        self.poluuid = poluuid
        self.sessionid = sessionid
        self.policyid = policyid
        self.policytype = policytype
        self.policymode = policymode
        self.service = service