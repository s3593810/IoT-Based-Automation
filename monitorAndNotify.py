from SenseEnvironment import SenseEnvironment
from SenseHatDB import SensehatDB, NotificationDB
from Read_Json_File import ReadJsonFile
from notification import Notification


class MonitorAndNotify:

    db = SensehatDB()
    db.createDatabase()
    notifyDB = NotificationDB()
    notifyDB.createDatabase()
    sense = SenseEnvironment()
    notifyUser = Notification()
    jsonVariables = ReadJsonFile()

# starttime = time.time()

    def isTempInRange(self, temp):
        if self.jsonVariables.min_temperature < temp < self.jsonVariables.max_temperature:
            return True
        else:
            return False

    def isHumInRange(self, hum):
        if self.jsonVariables.min_humidity < hum < self.jsonVariables.max_humidity:
            return True
        else:
            return False

    def tempStatusMessage(self, temp):
        if(temp < self.jsonVariables.min_temperature):
            tempDiffrence = self.jsonVariables.min_temperature-temp
            return "{} *C below minimum temperature".format(round(tempDiffrence, 1))
        elif(temp > self.jsonVariables.max_temperature):
            tempDiffrence = temp-self.jsonVariables.max_temperature
            return "{} *C above maximum temperature".format(round(tempDiffrence, 1))
        else:
            return None

    def humStatusMessage(self, hum):
        if(hum < self.jsonVariables.min_humidity):
            humDiffrence = ((self.jsonVariables.min_humidity-hum) /
                            self.jsonVariables.min_humidity)*100
            return "{} % below minimum humidity".format(round(humDiffrence, 1))
        elif(hum > self.jsonVariables.max_humidity):
            humDiffrence = ((hum-self.jsonVariables.max_humidity) /
                            self.jsonVariables.max_humidity)*100
            return "{} % above maximum humidity".format(round(humDiffrence, 1))
        else:
            return None

    def startApp(self):
        temp = self.sense.senseTmp()
        hum = self.sense.senseHum()
        while temp is None or hum is None:
            temp = self.sense.senseTmp()
            hum = self.sense.senseHum()
        if self.tempStatusMessage is None and self.humStatusMessage is None:
            self.db.insert(temp, hum, "OK", self.tempStatusMessage(
                temp), self.humStatusMessage(hum))
        else:
            self.db.insert(temp, hum, "BAD", self.tempStatusMessage(
                temp), self.humStatusMessage(hum))
        if self.notifyDB.search() is not True:
            if self.isTempInRange(temp) is False:
                self.notifyUser.send_notification_via_pushbullet(
                    "Temperature Warning", "The temperature now is {}".format(temp))
            if self.isHumInRange(hum) is False:
                self.notifyUser.send_notification_via_pushbullet(
                    "Humidity Warning", "The humidity now is {}".format(hum))
            self.notifyDB.insert('OK')

        self.db.displayDB()

        self.notifyDB.displayDB()


def main():
    s = MonitorAndNotify()
    s.startApp()


# Execute program.
if __name__ == "__main__":
    main()
