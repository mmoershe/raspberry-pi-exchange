# This uses the 7-Segment-Display
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(True)

NUM = [0xffc0,0xfff9,0xffa4,0xffb0,0xff99,0xff92,0xff82,0xfff8,0xff80,0xff90]
LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = 15      # DS Pin of 74HC595(Pin14)
latchPin  = 13      # ST_CP Pin of 74HC595(Pin12)
clockPin = 11       # CH_CP Pin of 74HC595(Pin11)


def setup():
    GPIO.setmode(GPIO.BOARD)   # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    
def destroy():
    GPIO.cleanup()
    print("Script wird beendet. Bye!")
    
def loop():
    print("loop:")
    #GPIO.output(dataPin, GPIO.HIGH)
    #GPIO.output(latchPin, GPIO.HIGH)
    #GPIO.output(clockPin, GPIO.HIGH)
    
def show_number(number):
    GPIO.output(latchPin, GPIO.LOW)
    for x in range(8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (NUM[number] >> x) & 1)
        GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
    
if __name__ == "__main__":
    print("starting...")
    setup()
    show_number(15)
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    destroy()
    