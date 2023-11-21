import time
import smbus
import PCA9685
import ServoPCA9685
from manipulator import manipulator

i2cBus = smbus.SMBus(3)
pca9685 = PCA9685.PCA9685(i2cBus)
servo15 = ServoPCA9685.ServoPCA9685(pca9685, PCA9685.CHANNEL15)
servo14 = ServoPCA9685.ServoPCA9685(pca9685, PCA9685.CHANNEL14)
# servo02 = ServoPCA9685.ServoPCA9685(pca9685, PCA9685.CHANNEL13)
# servo03 = ServoPCA9685.ServoPCA9685(pca9685, PCA9685.CHANNEL12)

# 130 -> 510
#for pulse in range(ServoPCA9685.servo_min, ServoPCA9685.servo_max + 1):

#servo00.set_pulse(299)
#    servo01.set_pulse(pulse)
#    servo02.set_pulse(pulse)
#    servo03.set_pulse(pulse)
#    time.sleep(0.01)
#servo00.set_angle(0)
# 510 -> 130
#for pulse in reversed(range(ServoPCA9685.servo_min, ServoPCA9685.servo_max + 1)):
#    servo00.set_pulse(pulse)
#    servo01.set_pulse(pulse)
#    servo02.set_pulse(pulse)
#    servo03.set_pulse(pulse)
#    time.sleep(0.01)


#for pulse in range(ServoPCA9685.servo_min, ServoPCA9685.servo_max + 1):
#   servo00.set_pulse(pulse)
#    time.sleep(0.01)

#for pulse in reversed(range(ServoPCA9685.servo_min, ServoPCA9685.servo_max + 1)):
#    servo00.set_pulse(pulse)
#    time.sleep(0.01)


servo15.set_angle(100)
time.sleep(2)
servo14.set_angle(0)
time.sleep(1)

def slow_angle(servos, angles):
    q = 0
    G = [0, 0]
    while G[0] < angles[0] or G[1] < angles[1]:
        for k, servo in enumerate(servos):
            servo.set_angle(G[k])
            time.sleep(0.1)
        if(G[0] < angles[0]):
            G[0]+=1
        if(G[1] < angles[1]):
            G[1]+=1

_, _, alpha, beta = manipulator(0, 5, 10, 0, 7, 10)
#slow_angle([servo00, servo01], [alpha, beta])

servo15.disable()
servo14.disable()
