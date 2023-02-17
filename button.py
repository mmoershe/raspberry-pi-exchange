import RPi.GPIO as GPIO
GPIO.setwarnings(False)
buttonPin = 37

GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
GPIO.setup(buttonPin, GPIO.IN)
print ("Bereit.")

while True: 
    if GPIO.input(buttonPin) == GPIO.LOW:
        print("Knopf wurde gedrückt.")


