import os, sys, time
from datetime import datetime
from sense_hat import SenseHat
import sqlite3 as lite

class SenseHatDB:
    dbname='sensehat.db'
    sampleFreq = 1 # time in seconds
    
    def createDatabase():
        con = lite.connect('sensehat.db')
        with con: 
            cur = con.cursor() 
            cur.execute("CREATE TABLE IF NOT EXISTS SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum Numeric)")
            
    def displayData():
        conn=lite.connect(dbname)
        curs=conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SenseHat_data"):
            print (row)
        conn.close()