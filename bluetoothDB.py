from datetime import datetime, timedelta
from abc import ABC
import sqlite3 as lite
from pytz import timezone

# Creating and managing a database which has mac addresses and timestamps for those devices have been notified


class BluetoothDB():
    database_name = 'bluetoothDB.db'

    def __init__(self):
        self.createDatabase()
    # Creating a database if it does not exist.

    def createDatabase(self):
        connection = lite.connect(self.database_name)
        with connection:
            point = connection.cursor()
            point.execute(
                "CREATE TABLE IF NOT EXISTS Notification_blutooth(macAddress VARCHAR(30), timestamp DATETIME)")

    # It is a multifunction method which is for inserting if mac address not recorded
    #  or update the time for an existing mac address
    def insert(self, macAddress):
        connection = lite.connect(self.database_name)
        with connection:
            if(self.search(macAddress)) is None:
                connection.execute(
                    "INSERT INTO Notification_blutooth values((?), (?))", (macAddress, datetime.now()))
            else:
                connection.execute(
                    "UPDATE Notification_blutooth SET (?) WHERE (?)", (datetime.now(), macAddress))
            connection.commit()
        connection.close()

    # Looking for a mac address to return which time is registered in the database.

    def search(self, macAddress):
        connection = lite.connect(self.database_name)
        with connection:
            point = connection.cursor()
            timeFound = point.execute(
                "SELECT time(timestamp) FROM Notification_blutooth WHERE macAddress == (?)", (macAddress,)).fetchone()
        connection.close()
        if timeFound is not None:
            return timeFound
        else:
            return None
