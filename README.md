# Connecting-Raspberry-Pi-with-Firebase-Database-Using-Python
The following project was developed to collect the humidity and the temperature using the DHT22 sensor and Raspberry Pi v3 and store these data on the Firebase database.
## The following instructions should work with any types of projects, since the basic idea has pretty much the same logic.
### My project setup:
1.	Raspberry Pi v3 model B, running Raspbian 4.9.35-v7.
2.	DHT22 sensor with 3 pins: GND, 5V and Data.
#### First, you must configure your Raspberry Pi with the following:

1.	sudo apt-get update
2.	sudo apt-get install python-dev
3.	wget https://bootstrap.pypa.io/get-pip.py
4.	sudo python get-pip OR sudo apt-get install python-pip (new Raspian versions)
5.	sudo pip install pyrebase #### Note that you may need to update your pyasn modules (pip install --upgrade pyasn1-modules)
6. I also had to download some files for the DHT22 sensor from github: https://github.com/adafruit/Adafruit_Python_DHT

##### If you are done with the previous steps, you are now ready to start writing the python script. Take a look at the following link for the pyrebase: https://github.com/thisbejim/Pyrebase.

```
# This code should be used with every script that you will be using to connect to the Firebase database.
import pyrebase
from firebase import firebase
config = {
  # You can get all these info from the firebase website. It's associated with your account.
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
.
.
.
.
```
 ##### Look at the Pyrebase https://github.com/thisbejim/Pyrebase to look at the functions and how to use them.
