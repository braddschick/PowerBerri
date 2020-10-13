import RPi.GPIO as GPIO
import time
# buttons={"twentySix": 26, "nineTeen": 19,"twenty": 20, "sixTeen": 16}
# GPIO.setmode(GPIO.BOARD)
# for btn in buttons:
#     # GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#     GPIO.add_event_detect(buttons.get(btn), GPIO.RISING, callback=btn)

buttons = [26, 16, 20, 19]

def callback(chnl):
    print(f"well {chnl} was called")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for btn in buttons:
    GPIO.add_event_detect(btn, GPIO.RISING, callback=callback, bouncetime=1000)

time.sleep(45)

GPIO.cleanup()