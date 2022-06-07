import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BOARD)

lightList = {
    "0": {
        "resistorPin": -1,
        "ledPin": -1,
        "led": None,
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "1": {
        "resistorPin": -1,
        "ledPin": -1,
        "led": None,
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "2": {
        "resistorPin": 13,
        "ledPin": 18,
        "led": LED(18),
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "3": {
        "resistorPin": 11,
        "ledPin": 23,
        "led": LED(23),
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "4": {
        "resistorPin": -1,
        "ledPin": -1,
        "led": None,
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "5": {
        "resistorPin": -1,
        "ledPin": -1,
        "led": None,
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    "6": {
        "resistorPin": -1,
        "ledPin": -1,
        "led": None,
        "haveToTake": False,
        "isOn": False,
        "firstLightValue": -1
    },
    
}