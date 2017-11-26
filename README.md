# Connecting-Raspberry-Pi-with-Firebase-Database-Using-Python
The following project was developed to collect the humidity and the temperature using the DHT22 sensor and Raspberry Pi v3 and store these data on the Firebase database.
The following instructions should work with any types of projects, since the basic idea has pretty much the same logic.
My project setup:
1.	Raspberry Pi v3 model B, running Raspbian 4.9.35-v7.
2.	DHT22 sensor with 3 pins: GND, 5V and Data.
First, you must configure your Raspberry Pi with the following:
sudo apt-get update
sudo apt-get install python-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip
sudo pip install pyrebase
```
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
```
