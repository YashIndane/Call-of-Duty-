# Call-of-Duty

![](https://img.shields.io/badge/license-MIT-yellowgreen)  ![](https://img.shields.io/badge/python-3.8-red) ![](https://img.shields.io/badge/impressions-135.5k-lightblue?style=flat&logo=linkedin) ![](https://img.shields.io/badge/likes-4.1k-lightblue?style=flat&logo=linkedin)

![codmr](https://user-images.githubusercontent.com/53041219/207020877-01cac301-04bd-4405-9bb3-d23b4fc3576a.jpg)

[Demo link](https://www.linkedin.com/feed/update/urn:li:activity:6779814634418401280/)

## Installations 

PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

```
$ pip install PyAutoGUI
```

```
$ pip install numpy
```

```
$ pip install SpeechRecognition
```

![demogif](https://user-images.githubusercontent.com/53041219/207021009-4b9fdac9-65e8-44d2-91be-5e7c7b105721.gif)

Download Bluestacks -> [link](https://www.bluestacks.com/)

After downloading Bluestacks open it and go to discover apps and search for Call of Duty and install it.


## Collecting data and building the model

We use the Sensor UDP app , that sends the selected sensor values to a receiving program using UDP. We use the orientation parameters.
After selecting Orientaion and filling the values, tap on send data.

![zz](https://user-images.githubusercontent.com/53041219/207021097-75bd0369-b814-45fa-8b91-8efc7fecd076.png)

Getting your ip - 

Type in CMD `ipconfig` and get you IP. Now we need trainig data for 5 positions or movements. So we will store the training data in `orientations.csv`
For each orientation, that is run the program `data_collector.py` 5 times for each move and be in that position for around `2 minutes`.

Enter your IP and port number for UDP data transmission in `data_collector.py`.


![movements](https://user-images.githubusercontent.com/53041219/207021206-bfeb8695-7bb7-4efd-8712-85df57b95a50.png)

## Training the SVM model

I have used Support Vector machine as it was giving good accuracy compared to others.

## Gameplay Settings

Start the game and go to settings > Controls and select `Simple Mode`.
Now start your Game and execute the `demo.py` file and enjoy!!

Open to PR's
