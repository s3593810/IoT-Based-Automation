from datetime import datetime
import sqlite3 as lite

class SensehatDB:
    __connection = lite.connect('sensehat.db')
    def createDatabase(self):
        with self.__connection: 
            point = self.__connection.cursor() 
            point.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")
            
    def InsertData (self,temp,hum):	
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