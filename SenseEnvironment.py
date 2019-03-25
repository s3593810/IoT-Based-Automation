import os, sys, time
from sense_hat import SenseHat

class SenseEnvironment:

      def getCPUtemperature(self):
        res = os.popen('vcgencmd measure_temp').readline()
        return(float(res.replace("temp=","").replace("'C\n","")))
	

      def sense(self):
        sense = SenseHat()
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        hum = sense.get_humidity()
        temp = temp - ((self.getCPUtemperature() - temp)/1)