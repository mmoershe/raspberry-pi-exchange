import os, sys, time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

PAUSE_LENGTH = 0.06
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
    for i in range(0,10):
        GPIO.output(cPin,GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH)
        
def loop():
    go_backwards = True
    x = 1
    while True:
        print(f"{x}\t{hex(x)}")
        GPIO.output(latchPin, GPIO.LOW)
        shiftOut(dataPin, clockPin, LSBFIRST, x)
        GPIO.output(latchPin, GPIO.HIGH)
        if hex(x) == "0x200" or hex(x) == "0x1":
            go_backwards = not go_backwards
            print("direction changed")
        if go_backwards:
            x>>=1
        else:
            x<<=1
        
        
        time.sleep(PAUSE_LENGTH) 
        
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
