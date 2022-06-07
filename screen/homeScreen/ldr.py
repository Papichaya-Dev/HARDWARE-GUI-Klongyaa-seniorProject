import RPi.GPIO as GPIO
import time
from gpiozero import LED

GPIO.setmode(GPIO.BOARD)

def getFirstLightValue(resistorPin):
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime
    result = diff * 1000
    return result

def pickPillDetection(firstLightValue, resistorPin, ledPin, led) :
    led.on()
    
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0

    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime
        
    result = diff * 1000
    
    # print('wtf ', result-firstLightValue)
    
    if firstLightValue == -1 :
        print("-1-1-1-1")
        firstLightValue = result
    else :
        if result-firstLightValue > 10 :
            led.off()
            return False
        else :
            led.on()
            return True
    