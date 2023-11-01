import os, sys, time
import RPi.GPIO as GPIO

GPIO.setwarnings(True)
ledPin = 11 # defining LED-Pin 
PAUSE_LENGTH: float = 0.5
LONG_LENGTH: float = 1.0
SHORT_LENGTH: float = 0.3

def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
    
def destroy():
    GPIO.cleanup()
    print("Script will be closed. Bye!")
    sys.exit()

def clear_terminal():
    # clear terminal while differentiating between linux and windows terminals
    if os.name == "nt":
        # windows
        os.system("cls")
    else:
        # alles andere
        os.system("clear")
        
def blink(length):
    if length not in [".", "-"]:
        print("--- blink() hat falsche Argumente erhalten ---")
        destroy()
        return 
    GPIO.output(ledPin, GPIO.HIGH)
    print(f"\t{length}")
    if length == ".":
        time.sleep(SHORT_LENGTH)
    elif length == "-":
        time.sleep(LONG_LENGTH)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(PAUSE_LENGTH)
    
alphabet: dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "\"": ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}
    

if __name__ == "__main__":
    setup()
    
    WORD: str = input("Bitte gib Text ein, welcher im Morsecode angezeigt werden soll:\t")
    WORD = "test" if WORD == "" else WORD
    
    clear_terminal()
    print(f"--> '{WORD}'", end="\n\n")
    
    for letter in WORD:
        if letter == " ":
            continue
        print(letter)
        try:
            for i in alphabet[letter.lower()]:
                blink(i)
        except KeyError:
            print(f"\t{letter.lower()} kenne ich nicht. Dieser Buchstabe wird uebersprungen.")
            continue
    destroy()