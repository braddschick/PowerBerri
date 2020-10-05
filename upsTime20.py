# Pi-UpTimeUPS UPS HAT
#
# Tested on Pi-UpTimeUPS v2.0
#

import RPi.GPIO as GPIO
import time
import os
import sys
import subprocess
import logging

buttonPin=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

schlaf=10
waitTime=1
while True:
    if (GPIO.input(buttonPin)):
        time.sleep(schlaf)
    else:
        logging.info("Power has been lost and will now start shutdown after the wait time")
        subprocess.call(f"shutdown -h {waitTime} &", shell=True)
        time.sleep(2)
        sys.stdout.flush()
        exit()
    sys.stdout.flush()
