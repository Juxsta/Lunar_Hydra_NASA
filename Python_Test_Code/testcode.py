#!/usr/bin/env python
import LCD1602
import PCF8591 as ADC
import time
import RPi.GPIO as GPIO
D0=17
GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)
    GPIO.setup (D0, GPIO.IN)
    LCD1602.init(0x27, 1)	# init(slave address, background light)
    #LCD1602.write(0, 0, 'Andorich')
    #LCD1602.write(1, 1, 'Sugondese')
    time.sleep(2)

def loop():
	#space = '                '
	#greetings = 'Thank you for buying SunFounder Sensor Kit for Raspberry! ^_^'
	#greetings = space + greetings
    while True:
        LCD1602.write(0,0,ADC.read(0))
        tmp = GPIO.input(D0)
        time.sleep(0.8)
        LCD1602.clear()
#for i in range(0, len(greetings)):
#	LCD1602.write(0, 0, tmp)
#	tmp = tmp[1:]
#	time.sleep(0.8)
#	LCD1602.clear()

def destroy():
        GPIO.cleanup(0)
        pass	

if __name__ == "__main__":
	try:
		setup()
		while True:
			pass
	except KeyboardInterrupt:
		destroy()
