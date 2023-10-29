import RPi.GPIO as GPIO
import time

motion_sensor = 17
led = 3

GPIO.setmode(GPIO.BCM)

#GPIO.setup(led,GPIO.OUT)

GPIO.setup(motion_sensor, GPIO.IN)

current_state = 0

#GPIO.output(led,False)


try:
	while True:
		time.sleep(2)
		current_state = GPIO.input(motion_sensor)
		if current_state == 1:
			print("GPIO pin %s is %s" % (motion_sensor, current_state))
			#GPIO.output(led,True)
		else:
			print("No motion")
			#GPIO.output(led,False)
			     
except KeyboardInterrupt:
	pass
finally:
	#GPIO.output(led,False)
	GPIO.cleanup()
