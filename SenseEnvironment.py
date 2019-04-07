import os
import sys
import time
from sense_hat import SenseHat

#  This class is getting a temperature and humidity reading using senseHat


class SenseEnvironment:
    __sense = SenseHat()
# getting CPU temperature which is used to get an accurate reading for the outside temperature

    def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(float(res.replace("temp=", "").replace("'C\n", "")))

        #  Reading temperature
    def senseTmp(self):
        temp = self.__sense.get_temperature()
        temp = temp - ((self.getCPUtemperature() - temp)/1)
        temp = round(temp, 1)
        return temp

 #  Reading humidity
    def senseHum(self):
        hum = self.__sense.get_humidity()
        hum = round(hum, 1)
        return hum
