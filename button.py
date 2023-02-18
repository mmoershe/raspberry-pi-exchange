import RPi.GPIO as GPIO
GPIO.setwarnings(False)
ledPin = 11
buttonPin = 37

GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.output(ledPin, GPIO.LOW)
print ("Bereit.")

while True: 
    if GPIO.input(buttonPin) == GPIO.LOW:
        GPIO.output(ledPin, GPIO.HIGH)
    else: 
        GPIO.output(ledPin, GPIO.LOW)