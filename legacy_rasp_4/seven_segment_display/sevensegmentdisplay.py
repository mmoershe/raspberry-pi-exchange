import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = 15      # DS Pin of 74HC595(Pin14)
latchPin  = 13      # ST_CP Pin of 74HC595(Pin12)
clockPin = 11       # CH_CP Pin of 74HC595(Pin11)
# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xffc0, 0xfff9,0xffa8,0xffb0,0xff99,0xff92, 0xff82,0xfff8, 0xff80,0xff90,0xff88,0xff83,0xffc6,0xffa1,0xff86,0xff8e,0xffe2,0xff8d,0xffcf,0xfff1,0xffc7,0xffc8,0xff8c,0xff98,0xffaf,0xff87,0xffc1,0xff91]

thisdict = {
  0: 0xffc0,
  1: 0xfff9,
  2: 0xffa8,
  3: 0xffb0,
  4: 0xff99,
  5: 0xff92,
  6: 0xff82,
  7: 0xfff8,
  8: 0xff80,
  9: 0xff90,
  "a": 0xff88,
  "b": 0xff83,
  "c": 0xffc6,
  "d": 0xffa1,
  "e": 0xff86,
  "f": 0xff8e,
  "g": 0xffe2,
  "h": 0xff8d,
  "i": 0xffcf,
  "j": 0xfff1,
  "l": 0xffc7,
  "n": 0xffc8,
  "p": 0xff8c,
  "q": 0xff98,
  "r": 0xffaf,
  "t": 0xff87,
  "U": 0xffc1,
  "y": 0xff91,
}

def setup():
    GPIO.setmode(GPIO.BOARD)   # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    
def shiftOut(dPin,cPin,order,val):
    for i in range(0,16):
        GPIO.output(cPin,GPIO.LOW);
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x8000&(val<<i)==0x8000) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH);

def loop():
    while True:
        for i in range(0,len(num)):
            GPIO.output(latchPin,GPIO.LOW)
            shiftOut(dataPin,clockPin,MSBFIRST,num[i])  # Send serial data to 74HC595
            GPIO.output(latchPin,GPIO.HIGH)
            time.sleep(0.5)   

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()  