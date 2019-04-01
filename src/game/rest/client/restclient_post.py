# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import requests
import json

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

text_no_goal = 'No goal'
text_goal_home = 'Goal home'
text_goal_away = 'Goal away'
text_game = 'Game 1'

print "goal test [press ctrl+c to end]"

# main program loop
try:
    while True:
        # no goal
        if GPIO.input(GPIO_PIN_HOME_TEAM) == True and GPIO.input(GPIO_PIN_AWAY_TEAM) == True:
            print text_no_goal
        # goal home
        elif GPIO.input(GPIO_PIN_HOME_TEAM) == False:
            print text_goal_home
            payload = {text_game: text_goal_home}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print response.text
        # goal away
        elif GPIO.input(GPIO_PIN_AWAY_TEAM) == False:
            print text_goal_away
            payload = {text_game: text_goal_away}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print response.text
        print "---------------------------------------"
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()