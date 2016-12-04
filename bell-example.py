import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def play_bell():
    # subprocess.call('/usr/bin/mpg123 /home/pi/button/doorbell.mp3', shell=True)
    subprocess.Popen('/usr/bin/mpg123 /home/pi/button/doorbell.mp3', shell=True)

pressed = False


try:
    while True:
        input_state = GPIO.input(18)
        if (not pressed) and input_state == False:
            print('Button Pressed')
            pressed = True
            play_bell()
            time.sleep(0.2)
        elif pressed and input_state == True:
            pressed = False
            print('Button Released')
            time.sleep(0.2)
finally:
    GPIO.cleanup()
    print('cleaned up')

