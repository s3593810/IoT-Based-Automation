import json
from pathlib import Path

# Reading Json file


class ReadJsonFile():

    def __init__(self):
        data = self.__read()
        self.__min_temperature = data["min_temperature"]
        self.__max_temperature = data["max_temperature"]
        self.__min_humidity = data["min_humidity"]
        self.__max_humidity = data["max_humidity"]

    @classmethod
    def __read(self):
        try:
            variables = json.loads(Path("config.json").read_text())
            return variables

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
