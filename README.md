# Call-of-Duty

![](https://img.shields.io/badge/license-MIT-yellowgreen)  ![](https://img.shields.io/badge/python-3.8-red)

![](images/codmr.jpg)

Download Bluestacks -> [link](https://www.bluestacks.com/)

After downloading Bluestacks open it and go to discover apps and search for Call of Duty and install it.


## Collecting data and building the model

We use the Sensor UDP app , that sends the selected sensor values to a receiving program using UDP. We use the orientation parameters.
After selecting Orientaion and filling the values, tap on send data.

![](images/zz.png)

Getting your ip - 

Type in CMD `ipconfig` and get you IP. Now we need trainig data for 5 positions or movements. So we will store the training data in `orientations.csv`
For each orientation, that is run the program `data_collector.py` 5 times for each move and be in that position for around `2 minutes`.

Enter your IP and port number for UDP data transmission in `data_collector.py`.


![](movements.png)

## Training the SVM model

I have used Support Vector machine as it was giving good accuracy compared to others.







[Demo link](https://www.linkedin.com/feed/update/urn:li:activity:6779814634418401280/)
