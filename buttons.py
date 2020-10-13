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
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(26, GPIO.RISING, callback=callback)
GPIO.add_event_detect(19, GPIO.RISING, callback=callback)
GPIO.add_event_detect(20, GPIO.RISING, callback=callback)
GPIO.add_event_detect(16, GPIO.RISING, callback=callback)

time.sleep(45)

GPIO.cleanup()