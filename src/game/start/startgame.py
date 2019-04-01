# Needed modules will be imported and configured
import RPi.GPIO as GPIO

# Referring to the pins by the "Broadcom SOC channel" number
GPIO.setmode(GPIO.BCM)
# Declaration of the input pins which are connected with the two IR sensors (home/away team)
GPIO_PIN_HOME_TEAM = 25
GPIO_PIN_AWAY_TEAM = 17
GPIO.setup(GPIO_PIN_HOME_TEAM, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_AWAY_TEAM, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
print "goal test [press ctrl+c to end]"
 
# main program loop
try:
        while True:
            # no goal
            if GPIO.input(GPIO_PIN_HOME_TEAM) == True and GPIO.input(GPIO_PIN_AWAY_TEAM) == True:
                print "No goal"
            # goal home
            elif GPIO.input(GPIO_PIN_HOME_TEAM) == False:
                print "Goal home"
            # goal away
            elif GPIO.input(GPIO_PIN_AWAY_TEAM) == False:
                print "Goal away"
            print "---------------------------------------"
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()