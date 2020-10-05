# Pi-UpTimeUPS UPS HAT
#
# Tested on Pi-UpTimeUPS v2.0
#

import RPi.GPIO as GPIO
import time
import os
import sys
import subprocess

butonPin=37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

schlaf=10
waitTime=15
while True:
    if (GPIO.input(buttonPin)):
        time.sleep(schlaf)
    else:
        subprocess.call(f"shutdown -h {waitTime} &", shell=True)
        time.sleep(2)
        sys.stdout.flush()
        exit()
    sys.stdout.flush()
