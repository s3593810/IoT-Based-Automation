from datetime import datetime, timedelta
from abc import ABC
import sqlite3 as lite
from pytz import timezone


class DataBase(ABC):
    _localTime = datetime.now(
        timezone('Australia/Sydney')).strftime("%Y-%m-%d %H:%M:%S")
    _databaseName = 'sensehat.db'
    #   @abstractmethod

    def createDatabase(self):
        pass
#   @abstractmethod

    def insert(self):
        pass
#   @abstractmethod

    def displayDB(self):
        pass


class SensehatDB(DataBase):

    def createDatabase(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric, status VARCHAR(10), temMessage VARCHAR(255),humMessage VARCHAR(255))")

    def insert(self, temp, hum, status, tempMessage, humMessage):
        connection = lite.connect(self._databaseName)
        with connection:
            connection.execute(
                "INSERT INTO SENSEHAT_data values((?), (?), (?), (?), (?), (?))", (self._localTime, temp, hum, status, tempMessage, humMessage,))
            connection.commit()
        connection.close()

# This code is taken from Tute sheet example
# for week4 which is created by Mathew that for learning purposes

    def reportDB(self):
        connection = lite.connect(self._databaseName)
        DATE_FORMAT = "%Y-%m-%d"
        ONE_DAY_DELTA = timedelta(days=1)
        data = {}
        with connection:
            cursor = connection.cursor()

            row = cursor.execute(
                "SELECT DATE(MIN(timestamp)), DATE(MAX(timestamp)) FROM SenseHat_data").fetchone()
            startDate = datetime.strptime(row[0], DATE_FORMAT)
            endDate = datetime.strptime(row[1], DATE_FORMAT)
            date = startDate
            while date <= endDate:
                row = cursor.execute(
                    """SELECT status,temMessage, humMessage FROM SenseHat_data
                WHERE timestamp >= DATE(:date) AND timestamp < DATE(:date, '+1 day')""",
                    {"date": date.strftime(DATE_FORMAT)}).fetchone()
                oneRow = [row[0], row[1], row[2]]
                data[date.strftime(DATE_FORMAT)] = oneRow
                date += ONE_DAY_DELTA
        connection.close()
        return data


class NotificationDB(DataBase):

    def createDatabase(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            point.execute(
                "CREATE TABLE IF NOT EXISTS Notification_data(timestamp DATETIME, status VARCHAR(10))")

    def insert(self, status):
        connection = lite.connect(self._databaseName)
        with connection:
            connection.execute("INSERT INTO Notification_data values((?), (?))",
                               (self._localTime, status))
            connection.commit()
        connection.close()

    def displayDB(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            print("\nEntire database contents:\n")
            for row in point.execute("SELECT * FROM Notification_data"):
                print(row)
        connection.close()

    def search(self):
        connection = lite.connect(self._databaseName)
        with connection:
            point = connection.cursor()
            s = point.execute("SELECT * FROM Notification_data WHERE date(timestamp) == (?)", (datetime.now(
                timezone('Australia/Sydney')).date(),)).fetchone()
        connection.close()
        if s is not None:
            return True
