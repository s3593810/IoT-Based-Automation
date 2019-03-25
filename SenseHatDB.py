from datetime import datetime
import sqlite3 as lite

class SensehatDB:
    
     def createDatabase(self):
        con = lite.connect('sensehat.db')
        with con: 
            cur = con.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")