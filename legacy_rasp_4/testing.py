# This uses the 7-Segment-Display
import RPi.GPIO as GPIO
import time

# GPIO.setwarnings(True)

NUM = [0xffc0,0xfff9,0xffa4,0xffb0,0xff99,0xff92,0xff82,0xfff8,0xff80,0xff90]
LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = 15      # DS Pin of 74HC595(Pin14)
latchPin  = 13      # ST_CP Pin of 74HC595(Pin12)
clockPin = 11       # CH_CP Pin of 74HC595(Pin11)

def destroy():
    GPIO.cleanup()
    print("--- Script will be closed. Bye! ---")
def setup():
    GPIO.setmode(GPIO.BOARD)   # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    GPIO.output(dataPin, GPIO.LOW)   
    GPIO.output(latchPin, GPIO.LOW)
    GPIO.output(clockPin, GPIO.LOW)
    
def onoff():
    GPIO.output(clockPin, GPIO.HIGH)
    GPIO.output(clockPin, GPIO.LOW)

if __name__ == "__main__":
    print("--- Script is starting. ---")
    setup()
    
    GPIO.output(dataPin, GPIO.HIGH)
    onoff()
    onoff()
    onoff()
    onoff()
    GPIO.output(dataPin, GPIO.LOW)
    onoff()
    onoff()
    onoff()
    GPIO.output(dataPin, GPIO.HIGH)
    onoff()
    onoff()
    onoff()
    onoff()
    onoff()
    onoff()
    onoff()    
    
    GPIO.output(latchPin, GPIO.HIGH)
    time.sleep(2)
    destroy()
