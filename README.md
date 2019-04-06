Monitor and Notify file is most crucial for this project.

This file handles most of the functionality of this project. 

Initially it checks using isTempInRange fuction whether the temperature is in the range comparing with the given json file. 
Later on it checks whether the humidity is in the given range or not using isHumInRange function.

Uisng tempStatusMessage and humStatusMessage functionality it sends status messege to keep it as a record in the database.

At the end using startApp function this file checks on temperature and humidity using sensehat sensors and there is multiple 
checking mechanism if the appropriate messege to send and when to send notifications using pushbiullets. 
