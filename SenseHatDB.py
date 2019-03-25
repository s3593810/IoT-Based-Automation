from datetime import datetime
import sqlite3 as lite

class SensehatDB:

     def createDatabase(self):
        connection = lite.connect('sensehat.db')
        with connection: 
            point = connection.cursor() 
            point.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")
            
        def InsertData (self,temp,hum):	
            Lconn=lite.connect('sensehat.db')
            point=connection.cursor()
            point.execute("INSERT INTO SENSEHAT_data values((?), (?), (?))", (datetime.now(), temp,hum,))
            connection.commit()
            connection.close()

        def displayDB(self):
            connection=lite.connect('sensehat.db')
            point=connection.cursor()
            print ("\nEntire database contents:\n")
            for row in point.execute("SELECT * FROM SenseHat_data"):
                print (row)
            connection.close()