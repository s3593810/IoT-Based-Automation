from datetime import datetime
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
               "CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")

   def insert(self, temp, hum):
       connection = lite.connect(self._databaseName)
       with connection:
           connection.execute(
               "INSERT INTO SENSEHAT_data values((?), (?), (?))", (self._localTime, temp, hum,))
           connection.commit()
       connection.close()

   def displayDB(self):
       connection = lite.connect(self._databaseName)
       with connection:
           point = connection.cursor()
           print("\nEntire database contents:\n")
           for row in point.execute("SELECT * FROM SenseHat_data"):
               print(row)
       connection.close()


class NotificationDB(DataBase):

   def createDatabase(self):
       connection = lite.connect(self._databaseName)
       with connection:
           point = connection.cursor()
           point.execute(
               "CREATE TABLE IF NOT EXISTS Notification_data(timestamp DATETIME, status VARCHAR(10), message VARCHAR(255))")

   def insert(self, status, message):
       connection = lite.connect(self._databaseName)
       with connection:
           connection.execute("INSERT INTO Notification_data values((?), (?), (?))",
                              (self._localTime, status, message))
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




