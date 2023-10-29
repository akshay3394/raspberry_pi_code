from gpiozero import MotionSensor
from time import sleep


def on_motion():
	print("Motion detected..")

pir = MotionSensor(17)

print("Starting..")

pir.when_activated = on_motion

try:
	while True:
		pir.wait_for_motion()
		print("Motion detected")
		pir.wait_for_no_motion()
		print("No motion detected")

except KeyboardInterrupt:
	print("Stopping..")
	





