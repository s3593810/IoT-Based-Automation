import json
from pathlib import Path

# Reading Json file


class ReadJsonFile():
    def __init__(self):
        self.__min_temperature, self.__max_temperature, self.__min_humidity, self.__max_humidity = self.__read()

    @classmethod
    def __read(self):
        try:
            data = Path("config.json").read_text()
            variables = json.loads(data)
            __newlist = []
            for key, value in variables.items():
                __newlist.append(value)
            return __newlist
        except FileNotFoundError:
            print("The file is Not Found")

    @property
    def min_temperature(self):
        return self.__min_temperature

    @property
    def max_temperature(self):
        return self.__max_temperature

    @property
    def min_humidity(self):
        return self.__min_humidity

    @property
    def max_humidity(self):
        return self.__max_humidity


read1 = ReadJsonFile()
print(read1.max_humidity)
