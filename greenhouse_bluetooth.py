import subprocess as sp
import os
from SenseEnvironment import SenseEnvironment
import re
import time
import bluetooth
from notification import Notification
from datetime import datetime, timedelta
from bluetoothDB import BluetoothDB

# This class is looking for the surrounding Bluetooth devices which are paired with Raspberry pi
#  and then send a notification every hour to them


class Greenhouse_bluetooth:
    db = BluetoothDB()
    # It checks if the user notifies during the last one hour or not.

    def isInOneHour(self, macAddress):
        notifyTime = self.db.search(macAddress)
        #  if the user does not have any record in the database.
        if notifyTime is None:
            return False
        else:
            # the user has a record then that record is checked if it within an hour or not.
            one_hour_after = datetime.now() + timedelta(hours=1)
            one_hour_after.strftime('%H:%M:%S')
            if notifyTime[0] < str(one_hour_after):
                return True
            else:
                return False
    # starts point for the class

    def main(self):
        sense = SenseEnvironment()
        notify = Notification()
        while True:
            # to get all devices which are paired with raspberry pi.
            p = sp.Popen(["bt-device", "--list"], stdin=sp.PIPE,
                         stdout=sp.PIPE, close_fds=True)
            (stdout, stdin) = (p.stdout, p.stdin)
            data = stdout.readlines()
            # Get the mac address as a string
            str_mac = str(data)
            str_mac = str(re.findall("\((.*?)\)", str_mac))
            str_mac = str_mac[2:len(str_mac)-2]
            # searching for surrounding Bluetooth devices
            nearbyDevices = bluetooth.discover_devices()
            for macAddress in nearbyDevices:
                # checking if the mac address founded is matching the one already paired.
                if macAddress == str_mac:
                    if self.isInOneHour(macAddress) is False:
                        temp = sense.senseTmp()
                        hum = sense.senseHum()
                        notify.send_notification_via_pushbullet(
                            "", " The temperature is {} and the humidity is {}".format(temp, hum))
                        self.db.insert(str_mac)
            # 20 sec before next scanning
            time.sleep(20)


# Execute program
Greenhouse_bluetooth().main()
