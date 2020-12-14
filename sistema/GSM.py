import RPi.GPIO as GPIO
import serial
import time
import sys
import datetime


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)


# SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)
setup()
ser.write("AT+CMGF=1\r")  # set to text mode
time.sleep(3)
ser.write('AT+CMGDA="DEL ALL"\r')  # delete all SMS
time.sleep(3)
ser.write('AT+CMGS="+593981849336"\r')
time.sleep(3)
msg = "Sending status at " + t + ":--" + state
print("Sending SMS with status info:" + msg)
ser.write(msg + chr(26))
