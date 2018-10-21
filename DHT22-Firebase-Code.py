# Author: Ahmed M. Hussain, All rights reserved 

import pyrebase
import sys
import Adafruit_DHT
import time

config = {
  "apiKey": "AIzaSyD68dO5eqaIPqa4KBm9DE0kt5U-aee2ooA",
  "authDomain": "tempapp-a0c0e.firebaseapp.com",
  "databaseURL": "https://tempapp-a0c0e.firebaseio.com",
  "storageBucket": "tempapp-a0c0e"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
while 1:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        data = {"Date": date_mmddyyyy,"Time": time_hhmmss, "Temperature": temperature, "Humidity": humidity}
        db.child("/message").push(data)
        print("Temp: %f -- Date: %s  -- Time: %s" %(x,date_mmddyyyy,time_hhmmss))
        time.sleep(60)
