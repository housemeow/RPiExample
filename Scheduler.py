import RPi.GPIO as GPIO
import time

def bin2dec(string_num):
    return int(string_num, 2)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

high_counter = 0
low_counter = 0

while True:
	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,GPIO.HIGH)
	time.sleep(0.025)
	GPIO.output(4,GPIO.LOW)
	time.sleep(0.02)

	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	data = []
	for i in range(0,500):
	    data.append(GPIO.input(4))

	index = 0
	humidity_bit = ""
	temperature_bit = ""
	crc = ""

	try:
		while data[index] == GPIO.HIGH:
			index = index + 1

		for i in range(0, 32):
			while data[index] == GPIO.LOW:
				index = index + 1

			high_bit_count = 0
			while data[index] == GPIO.HIGH:
				high_bit_count = high_bit_count + 1
				index = index + 1

			if high_bit_count > 3:
				if 0<=i and i<8:
					humidity_bit = humidity_bit + "1"
				if 16<=i and i<24:
					temperature_bit = temperature_bit + "1"
			else:
				if 0<=i and i<8:
					humidity_bit = humidity_bit + "0"
				if 16<=i and i<24:
					temperature_bit = temperature_bit + "0"
	except:
		#print "ERR_RANGE"
		continue
		#pass

	try:
		for i in range(0, 8):
			while data[index] == GPIO.LOW:
				index = index + 1

			high_bit_count = 0
			while data[index] == GPIO.HIGH:
				high_bit_count = high_bit_count + 1
				index = index + 1

			if high_bit_count > 3:
				crc = crc + "1"
			else:
				crc = crc + "0"
	except:
		#print "ERR_RANGE"
		continue
		# pass

	Humidity = bin2dec(humidity_bit)
	Temperature = bin2dec(temperature_bit)

	if Humidity + Temperature - bin2dec(crc) == 0:
		print "Humidity:"+ str(Humidity) +"%"
		print "Temperature:"+ str(Temperature) +"C"
		if Temperature >31:
			high_counter = high_counter+1
			low_counter = 0
		elif Temperature<=29:
			low_counter = low_counter+1
			high_counter = 0
		else:
			low_counter = 0
			high_counter = 0
		if high_counter >= 3:
			GPIO.output(14, GPIO.LOW)
			print "Tempterture is Too High, turn off the light"
		elif low_counter >= 3:
			GPIO.output(14, GPIO.HIGH)
			print "Temperture is Too Low, turn on the light"
		else:
			print "Unstable State"
		print ""
	#else:
		#print "ERR_CRC"


	time.sleep(1)