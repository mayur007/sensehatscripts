import RPi.GPIO as GPIO
import dht11
from datetime import datetime
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 4)
result = instance.read()

while(1):
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        data = str(result.temperature) +','+ str(result.humidity) +','+ str(datetime.now())
        with open('temperature_test.csv', 'a') as tfile:
            tfile.write(data)
	    tfile.write('\n')
        tfile.close()
    else:
        print("Error: %d" % result.error_code)
    time.sleep(1)

GPIO.cleanup()
