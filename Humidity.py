from sense_hat import SenseHat
import Environment

class Humidity(Environment):
    def Read(self):
        super().Read()
        sense = SenseHat()
        sense.clear()
        humidity = sense.get_humidity()
        print(humidity)
x=Humidity()
x.Read()
