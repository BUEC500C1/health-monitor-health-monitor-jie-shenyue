# Health-Monitor
- Database/Alert/Prediction: Jie Lu(jielu666@bu.edu)
- Display/Sensor: Shenyue Shao

# Sensor
In the Sensor module, use the random function to create the number from the range.

# Firebase
This project uses Firebase as our database. Everytime the data from the Sensors will send to our firebase platform.
![database_image](https://github.com/BUEC500C1/health-monitor-health-monitor-jie-shenyue/blob/master/databse_image.png)

# Display
Everytime the program get the data from our Database. The data first will pass to our Alert function. If every single data is normal, then it will display the data on our console.

# Alert
The standard of normal data is already described in the code.

# Prediction
In the prediction function, we use the mean of our data as the predict data. Use the panda module to create a dataframe and all the data in our database will put into this dataframe.
