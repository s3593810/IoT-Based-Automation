from SenseEnvironment import SenseEnvironment
from SenseHatDB import SensehatDB, NotificationDB
from Read_Json_File import ReadJsonFile
from notification import Notification
from App_Logging import SenseHatApp_logging


log = SenseHatApp_logging()
# This class is working as a driver class for other classes which are needed to complete the App functionality.


class MonitorAndNotify:
    # creating all object which is needed
    __db = SensehatDB()
    __notifyDB = NotificationDB()
    __sense = SenseEnvironment()
    __notifyUser = Notification()
    __jsonVariables = ReadJsonFile()
#  Checking the JSON file temperature range for current reading

    def __isTempInRange(self, temp):
        try:
            if self.__jsonVariables.min_temperature < temp < self.__jsonVariables.max_temperature:
                return True
            else:
                return False
        except Exception:
            # saving any error in the app log file
            log.logger.error("comparing the range of temperature has an error")
# Checking the JSON file humidity range for current reading

    def __isHumInRange(self, hum):
        try:
            if self.__jsonVariables.min_humidity < hum < self.__jsonVariables.max_humidity:
                return True
            else:
                return False
        except Exception:
            # saving any error in the app log file
            log.logger.error("comparing the range of humidity has an error")
#  o calculate the temperature difference between json values and current reading and return an appropriate message to be saved in the database

    def __tempStatusMessage(self, temp):
        try:
            if(temp < self.__jsonVariables.min_temperature):
                tempDiffrence = self.__jsonVariables.min_temperature-temp
                return "{} *C below minimum temperature".format(round(tempDiffrence, 1))
            elif(temp > self.__jsonVariables.max_temperature):
                tempDiffrence = temp-self.__jsonVariables.max_temperature
                return "{} *C above maximum temperature".format(round(tempDiffrence, 1))
            else:
                return None
        except Exception:
            # saving any error in the app log file
            log.logger.error("There is an error in tempStatusMessage")
# o calculate the humidity difference between json values and current reading and return an appropriate message to be saved in the database

    def __humStatusMessage(self, hum):
        try:
            if(hum < self.__jsonVariables.min_humidity):
                humDiffrence = ((self.__jsonVariables.min_humidity-hum) /
                                self.__jsonVariables.min_humidity)*100
                return "{} % below minimum humidity".format(round(humDiffrence, 1))
            elif(hum > self.__jsonVariables.max_humidity):
                humDiffrence = ((hum-self.__jsonVariables.max_humidity) /
                                self.__jsonVariables.max_humidity)*100
                return "{} % above maximum humidity".format(round(humDiffrence, 1))
            else:
                return None
        except Exception:
            # saving any error in the app log file
            log.logger.error("There is an error in humStatusMessage")
# The starting method in the App

    def startApp(self):
        try:
            # get temperature and humidity reading from senseHat
            temp = self.__sense.senseTmp()
            hum = self.__sense.senseHum()
            # Check if the reading none of them is null if so it will read again
            while temp is None or hum is None:
                temp = self.__sense.senseTmp()
                hum = self.__sense.senseHum()
            # inserting the reading values into the database with an appropriate message
            if self.__tempStatusMessage is None and self.__humStatusMessage is None:
                self.__db.insert(temp, hum, "OK", self.__tempStatusMessage(
                    temp), self.__humStatusMessage(hum))
            else:
                self.__db.insert(temp, hum, "BAD", self.__tempStatusMessage(
                    temp), self.__humStatusMessage(hum))

            # Check in the database if the user notify or not if it is not then it will be notified
            if self.__notifyDB.search() is not True:
                if self.__isTempInRange(temp) is False:
                    self.__notifyUser.send_notification_via_pushbullet(
                        "Temperature Warning", "The temperature now is {}".format(temp))
                if self.__isHumInRange(hum) is False:
                    self.__notifyUser.send_notification_via_pushbullet(
                        "Humidity Warning", "The humidity now is {}".format(hum))
                self.__notifyDB.insert('OK')
        except Exception:
            # saving any error in the app log file
            log.logger.error("There is an error in main method")


# Execute program.
if __name__ == "__main__":
    MonitorAndNotify().startApp()
