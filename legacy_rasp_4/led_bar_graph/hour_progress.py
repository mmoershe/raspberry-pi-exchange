import os, sys, time
import random
from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595
dataPin   = 15      # DS Pin of 74HC595(Pin14)
latchPin  = 13      # ST_CP Pin of 74HC595(Pin12)
clockPin = 11       # CH_CP Pin of 74HC595(Pin11)

def empty_led():
    GPIO.output(latchPin, GPIO.LOW)
    shiftOut(dataPin, clockPin, LSBFIRST, 0)
    GPIO.output(latchPin, GPIO.HIGH)

def destroy():
    empty_led()
    GPIO.cleanup()
    print("Script will be terminated. Bye!")
    sys.exit()
    
def setup():
    GPIO.setmode(GPIO.BOARD)    # use PHYSICAL GPIO Numbering
    GPIO.setup(dataPin, GPIO.OUT) # set pin to OUTPUT mode
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)
    empty_led()
    
# shiftOut function, use bit serial transmission. 
def shiftOut(dPin,cPin,order,val):
    GPIO.output(latchPin, GPIO.LOW)
    for i in range(0,10):
        GPIO.output(cPin,GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH)
    GPIO.output(latchPin, GPIO.HIGH)
        
def loop():
    INTERVAL_PAUSE = 1
    FAKTOR = 100/60
    values : dict = {
        0: 0,
        1: 512,
        2: 768,
        3: 896,
        4: 960,
        5: 992,
        6: 1008,
        7: 1016,
        8: 1020,
        9: 1022,
        10: 1023
    }
    
    while True:
        now = datetime.now()
        hour, minute, second = now.hour, now.minute, now.second
        print(f"{hour}:{minute}:{second} Uhr")
        progress: str = str(round(FAKTOR*second))
        if len(progress) == 1:
            progress = f"0{progress}"
        print(f"{progress}%", "------------", sep="\n")
        x = values[int(progress[0])]
        shiftOut(dataPin, clockPin, LSBFIRST, x)
        time.sleep(INTERVAL_PAUSE)


        
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    time.sleep(5)
    destroy()
