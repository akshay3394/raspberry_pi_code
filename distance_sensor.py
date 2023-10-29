import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setmode(GPIO.BCM)

TRG = 27
ECHO = 22

GPIO.setup(TRG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Measuring distance..")

try:
    #while True:

    GPIO.output(TRG, False)
    print("waiting for sensor to settle..")
    sleep(2)

    print("Starting")
    GPIO.output(TRG, True)
    sleep(0.00001)
    GPIO.output(TRG, False)
    
    print("waiing for echo high..")
    while GPIO.input(ECHO) == 0:
        start_time = time()

    print("waiing for echo low..")
    while GPIO.input(ECHO) == 1:
        end_time = time()

    duration = end_time - start_time

    print("Time difference : "+str(duration))

    distance = duration * 17150

    print("distance : "+str(round(distance, 2))+" cm")
    
    print("completed..")

except KeyboardInterrupt:
    print("Stopping..")

finally:
    
    GPIO.cleanup()
    print("cleaup")
