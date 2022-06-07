import RPi.GPIO as GPIO
import time
from gpiozero import LED

GPIO.setmode(GPIO.BOARD)

resistorPin = 11
led = LED(23)
led.on()
print("wtf")
#time.sleep(1)
#led.off()

buff = -1
isOn = True

while True:
    print("wtwtwt")
    #led turn on  
#     led.toggle()
#     time.sleep(0.1)
#     led.toggle()
#     time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0
    print("gegege")
    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime
    print("waer")
        
    def cal(pre, now):
        global isOn
        global buff
        global led
        
        print("wtf"+str(now-buff))
        
        if now-buff > 10 :
            print('if')
            led.off()
        else :
            print('else')
            led.on()
    
    result = diff * 1000
    
    if buff == -1 :
        buff = result
    else :
        cal(buff, result)
    
    
    print(diff * 1000)
    time.sleep(1)