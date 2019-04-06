import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

import seaborn as sns
import numpy as np
import pandas as pd
import sqlite3 as lite
from datetime import datetime
import re


class Analytics:

    connection = lite.connect('sensehat.db')
    c = connection.cursor()
        
    c.execute('SELECT timestamp, temp,hum FROM SENSEHAT_data')
    data = c.fetchall()

    date=[]
    temps = []
    hums = []
    for row in data:
        text = str(row)
        data = re.split(",",text)
            
        x = (data[0][8:12])
        date.append(x)
        temps.append(row[1])
        hums.append(row[2])

    def matplotlib_graph(self):
        plt.figure(1)
        plt.plot(self.date,self.hums, color='blue', linestyle='-', marker='o')
        plt.plot(self.date,self.temps, color='red', linestyle='-', marker='o')

        plt.ylabel('Temperature and Humidity')
        plt.xlabel('Date')
        plt.legend(["Humidity", "Temperature"])
        plt.suptitle('Changes in Humidity and Temperature')
        plt.tight_layout()
        plt.savefig('plot1.png')

    def seaborn_graph(self):
        plt.figure(2)
        plot = sns.lineplot(x=self.temps, y=self.hums, hue=self.date)
        plt.xlabel('Temperature')
        plt.ylabel('Humidity')
        plt.title('Temperature and Humidity Relations')
        fig = plot.get_figure()
        plt.tight_layout()
        fig.savefig('plot2.png')




