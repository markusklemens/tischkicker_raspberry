# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import requests
import json
import time

# Referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)
# Declaration of the input pins which are connected with the two IR sensors (home/away team)
GPIO_PIN_HOME_TEAM = 25
GPIO_PIN_AWAY_TEAM = 17
GPIO.setup(GPIO_PIN_HOME_TEAM, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_AWAY_TEAM, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Configure rest endpoint and json header
url = 'http://httpbin.org/post'
headers = {'content-type': 'application/json'}

# Goal counter vars
counterGoalHome = 0
counterGoalAway = 0

# Lables
textGoalHome = 'Goal home'
textGoalAway = 'Goal away'
textGame = 'Game 1'

# Timeout sleep in sec
timeoutSleepInSec = 0.3

# print function to show current score
def printScore():
    global counterGoalHome, counterGoalAway
    print 'Score Home vs. Away ' + str(counterGoalHome) + ':' + str(counterGoalAway)

# submit current score to rest endpoint
def submitScore():
    global payload, response
    payload = {textGame: printScore()}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print response.text

# sleep to avoid goal counter is triggered to often becuse IR sensor has very sensitive time span
def sleep():
    time.sleep(timeoutSleepInSec)

# main program loop
try:
    while True:
        # goal home
        if GPIO.input(GPIO_PIN_HOME_TEAM) == False:
            counterGoalHome += 1
            sleep()
            printScore()
            # submitScore()
        # goal away
        elif GPIO.input(GPIO_PIN_AWAY_TEAM) == False:
            counterGoalAway += 1
            sleep()
            printScore()
            # submitScore()

# Work after the end of the program when program exits with keyboard CTRL+D
except KeyboardInterrupt:
        printScore()
        submitScore()
        GPIO.cleanup()