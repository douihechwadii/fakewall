class Packet:
    def __init__(self, appid, app, appcat, apprisk, utmaction, countapp, devtype, osname, utmref):
        self.appid = appid
        self.app = app
        self.appcat = appcat
        self.apprisk = apprisk
        self.utmaction = utmaction
        self.countapp = countapp
        self.devtype = devtype
        self.osname = osname
        self.utmref = utmref