

class TemperatureSensor :
    def __init__  (self ):
        self._temperature = 0

    def check_temperature (self, temperature):
        self._temperature = temperature
        if self._temperature > 50:
            raise TemperatureError ('Temperature too high')
        else :
            print(f'Current temperature {self._temperature}')
sensor = TemperatureSensor()
try:
    sensor.check_temperature(55)
except TemperatureError as e:
    print (f'WARNING : {e}')