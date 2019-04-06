This file consists of severall classes 
1. DataBase class
2. SensehatDB Class and 
3. NotificationDB Class

The database class is basically an abstract class with some abstract methods created to handle the common behavior the the sensehatdb and 
notificationDB classes. 

It is designed such a way that createDatabase, insert values in database and display the values of the tables in database 
are the common behaviors for both of the child classes. 
Along with the common behaviors the sensehatDB class has the function called report function which keeps the track of notifications 
perday to create the csv file helping the report file. 

On the other hand the other notificationDB class additional search function to search through the existing data to find particular notification.


