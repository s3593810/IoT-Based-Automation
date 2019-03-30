from datetime import datetime
from abc import ABC
import sqlite3 as lite

class DataBase(ABC):
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
    __connection = lite.connect('sensehat.db')
   
    def createDatabase(self):
        with self.__connection: 
            point = self.__connection.cursor() 
            point.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")
            
    def insert (self,temp,hum):	
            point=self.__connection.cursor()
            point.execute("INSERT INTO SENSEHAT_data values((?), (?), (?))", (datetime.now(), temp,hum,))
            self.__connection.commit()
            self.__connection.close()

    def displayDB(self):
            point=self.__connection.cursor()
            print ("\nEntire database contents:\n")
            for row in point.execute("SELECT * FROM SenseHat_data"):
                print (row)
            self.__connection.close()


class NotificationDB(DataBase):
    __connection = lite.connect('sensehat.db')
   
    def createDatabase(self):
        with self.__connection: 
            point = self.__connection.cursor() 
            point.execute("CREATE TABLE IF NOT EXISTS Notification_data(timestamp DATETIME, status VARCHAR(10), message VARCHAR(600))")
            
    def insert (self,status,message):	
            point=self.__connection.cursor()
            point.execute("INSERT INTO Notification_data values((?), (?), (?))", (datetime.now(), status,message))
            self.__connection.commit()
            self.__connection.close()

    def displayDB(self):
            point=self.__connection.cursor()
            print ("\nEntire database contents:\n")
            for row in point.execute("SELECT * FROM Notification_data"):
                print (row)
            self.__connection.close()

