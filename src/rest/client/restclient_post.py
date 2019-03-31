# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import time
import requests
import json

GPIO.setmode(GPIO.BCM)

# Declaration of the input pin which is connected with the sensor.
GPIO_PIN = 25
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Break between the results will be defined here (in seconds)
delayTime = 0.2

# Configure rest endpoint and json header
url = 'http://httpbin.org/post'
headers = {'content-type': 'application/json'}

print "Tor-Test [press ctrl+c to end]"

# main program loop
try:
    while True:
        if GPIO.input(GPIO_PIN) == True:
            print "Kein Tor"
        else:
            print "Tor"
            payload = {'Spiel 1': 'Tor'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print response.text
        print "---------------------------------------"

        # Reset + Delay
        time.sleep(delayTime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()