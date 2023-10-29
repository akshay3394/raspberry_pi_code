from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory 
from time import sleep
import math

#sudo pigpiod

pin_factory = PiGPIOFactory()

servo = AngularServo(17, pin_factory=pin_factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

#servo = AngularServo(17, pin_factory=pin_factory)


try:
	while True:
		for i in range(0, 360):
			servo.value = math.sin(math.radians(i))
			sleep(0.005)

except KeyboardInterrupt:
	servo.angle = 0	
	servo.close()
	print("Program stopped")

# val = -1

# try:
# 	while True:
		# servo.value = val
		# sleep(1)
		# val = val + 0.1
		# if val > 1:
		# 	val = -1
		
# 		servo.min()
# 		sleep(2)
		
# 		servo.mid()
# 		sleep(2)

# 		servo.max()
# 		sleep(2)

# except KeyboardInterrupt:
# 	servo.close()
# 	print("Program stopped")
