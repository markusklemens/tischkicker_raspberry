# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import requests
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
textGame = 'team'

# Timeout sleep in sec
timeoutSleepInSec = 0.3

# print function to show current score
def printScore(goal):
    global counterGoalHome, counterGoalAway
    print goal

# submit current score to rest endpoint
def submitScore(value):
    try:
        global payload
        payload = {textGame: value}
        print payload
        response = requests.post(url, data=payload, headers=headers)
        print response.text
    except:
        print sys.exc_info()[0]

# sleep to avoid goal counter is triggered to often becuse IR sensor has very sensitive time span
def sleep():
    time.sleep(timeoutSleepInSec)

# main program loop
try:
    while True:
        # goal home
        if GPIO.input(GPIO_PIN_HOME_TEAM) == False:
            sleep()
            printScore('home')
            submitScore('home')
        # goal away
        elif GPIO.input(GPIO_PIN_AWAY_TEAM) == False:
            sleep()
            printScore('away')
            submitScore('away')

# Work after the end of the program when program exits with keyboard CTRL+D
except:
    print ''