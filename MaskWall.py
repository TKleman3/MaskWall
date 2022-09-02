import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c, address=0x42)

pca.frequency = 50

top = servo.Servo(pca.channels[0])
middle = servo.Servo(pca.channels[1])
bottom = servo.Servo(pca.channels[2])

n = 0

def moveServo(start,end,delta):
    incMove = (end-start)/100.0
    incTime = delta/100.0
    for x in range(100):
        top.angle = start + x*incMove
        middle.angle = start - x*incMove
        bottom.angle = start + x*incMove
        time.sleep(incTime)
    for x in range(100):
        top.angle = end - x*incMove
        middle.angle = (start-(end-start)) + x*incMove
        bottom.angle = end - x*incMove
        time.sleep(incTime)
    for x in range(100):
        top.angle = start - x*incMove
        middle.angle = start - x*incMove
        bottom.angle = start - x*incMove
        time.sleep(incTime)
    for x in range(100):
        top.angle = (start-(end-start)) + x*incMove
        middle.angle = (start-(end-start)) + x*incMove
        bottom.angle = (start-(end-start)) + x*incMove
        time.sleep(incTime)

playing = True
while playing:
    moveServo(45,60,5)
    

pca.deinit()
pca.reset()