from sense_hat import SenseHat

class SenseEnvironment:

      def sense(self):
        sense = SenseHat()
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        hum = sense.get_humidity()