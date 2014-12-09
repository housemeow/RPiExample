import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

# while True:
for i in range(0, 150):
	GPIO.output(15, 1)
	time.sleep(0.0025)
	GPIO.output(15, 0)
	time.sleep(0.0175)

p = GPIO.PWM(15, 50)#pin15, 50Hz
p.start(7.5)#duty cycle 7.5%

for i in range(0, 300):
	p.ChangeDutyCycle(7.5)
	time.sleep(1)
	p.ChangeDutyCycle(12.5)
	time.sleep(1)
	p.ChangeDutyCycle(2.5)
	time.sleep(1)

GPIO.cleanup()