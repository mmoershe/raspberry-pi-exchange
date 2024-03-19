import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
ledPin = 11 # define ledPin

def setup():
	GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
	GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
	GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
	print ('using pin%d'%ledPin)
	
def turnon():
	while True:
		GPIO.output(ledPin, GPIO.HIGH) # make ledPin output HIGH level to turn on led
		time.sleep(10)
		
def destroy():
	GPIO.cleanup() # Release all GPIO
	

if __name__ == '__main__': # Program entrance
	print ('LED wird angemacht...')
	setup()
	try:
		turnon()
	except KeyboardInterrupt: # Press ctrl-c to end the program.
		destroy()
