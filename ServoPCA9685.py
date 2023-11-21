import time
# Servo with PCA9685 implementation

# Configure min and max servo pulse lengths
servo_min = 130 # Min pulse length out of 4096 / 150/112
servo_max = 510 # Max pulse length out of 4096 / 600/492

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min + 1) / (in_max - in_min + 1) + out_min

class ServoPCA9685(object):
    def __init__(self, pca9685, channel):
        self.pca9685 = pca9685
        self.channel = channel
        self.set_pwm_freq(50)
        self.set_pulse(300)

    def set_pwm_freq(self, freq=50):
        self.pca9685.set_pwm_freq(freq)
        time.sleep(0.005)

    def set_angle(self, angle):
        self.set_pulse(map(angle, 0, 180, servo_min, servo_max))

    def set_pulse(self, pulse):
        if pulse >= servo_min and pulse <= servo_max:
            self.pca9685.set_pwm(self.channel, 0, pulse)
            time.sleep(0.005)

    def disable(self):
        self.pca9685.set_pwm(self.channel, 0, 0)
        time.sleep(0.005)
