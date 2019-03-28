import os, sys, time
from sense_hat import SenseHat

class SenseEnvironment:
      __sense = SenseHat()
      def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(float(res.replace("temp=","").replace("'C\n","")))
	
      def senseTmp(self):
        
        temp = self.__sense.get_temperature()
        temp = temp - ((self.getCPUtemperature() - temp)/1)
        temp = round(temp, 1)
        return temp
      
      def senseHum(self):
        hum = self.__sense.get_humidity()
        hum = round(hum,1)
        return hum