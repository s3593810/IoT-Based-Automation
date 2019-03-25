from datetime import datetime
import sqlite3 as lite

class SensehatDB:

     def createDatabase(self):
        con = lite.connect('sensehat.db')
        with con: 
            cur = con.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")
            
        def InsertData (self,temp,hum):	
            conn=lite.connect('sensehat.db')
            curs=conn.cursor()
            curs.execute("INSERT INTO SENSEHAT_data values((?), (?), (?))", (datetime.now(), temp,hum,))
            conn.commit()
            conn.close()

        def displayDB(self):
            conn=lite.connect('sensehat.db')
            curs=conn.cursor()
            print ("\nEntire database contents:\n")
            for row in curs.execute("SELECT * FROM SenseHat_data"):
                print (row)
            conn.close()