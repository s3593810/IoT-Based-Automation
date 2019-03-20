from sense_hat import SenseHat
#import Environment
class Temperature(Environment):
    def Read(self):
        super().Read()
        sense = SenseHat()
        sense.clear()
        temp = sense.get_temperature()
        print(temp)

x = Temperature()
x.Read()
 


