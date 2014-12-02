import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT, initial=0)

value = input("switch:")
while (value==0 or value==1):
	GPIO.output(14, value)
	value = input("switch:")
#GPIO.output(14, 0)



GPIO.cleanup()