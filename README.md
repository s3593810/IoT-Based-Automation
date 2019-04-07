
Monitor and Notify file is most crucial for this project.

This file handles most of the functionality of this project.

Initially it checks using isTempInRange fuction whether the temperature is in the range comparing with the given json file. Later on it checks whether the humidity is in the given range or not using isHumInRange function.

Uisng tempStatusMessage and humStatusMessage functionality it sends status messege to keep it as a record in the database.

At the end using startApp function this file checks on temperature and humidity using sensehat sensors and there is multiple checking mechanism if the appropriate messege to send and when to send notifications using pushbiullets.

JSON file

This json file keeps the limit of minimum and maximum humidity and temperature based on these limits the api and the code decides whether to send the user notification or not.

Read from the JSON File
In this file its all basically reades from the JSON file to python file.

SenseEnvironment file

This file calls for raspberry to get the data for humidity and temerature. The temperature of the environment gets caliberated using a function which first gets the sensed temperature along with the heat of the cpu. Later on delating or subtracting the tmeperature of the cpu helps getting the temperature value closer to the actual sourrounding temperature.

senseHatDB file
Creats SenseHat DataBase to insert sensed data from the sensor.

Analytics file

This branch works on visualization of data using python libraries. The sensehat data is saved in the data base. This branch reads the data from the database formats it into date, temperature and humidity and represents the changes in the temperature and humidity by days.

Two libraries are used to visualize the data. Matplotlib and sesborn library.

Matplotlib: Matplotlib is a 2-D plotting visualizing library. It emulates matlab like graphs and visualizations. Matplot library has robust plotting capacity. It is really good at representing data directly from database or csv files. It can represent differnt plots on the same figure using subplotting mechanism which is really helpful to present robust information in one picture. However it is only possilbe to represent 6 subplots in a figure using this library.

Seaborn Library: Seaborn is a statistical data visualization library. Although it stands on top of matplot library but it is good at representing statistical graphics in python. It is a dataset oriented api good at presenting relationships between multiple variables.