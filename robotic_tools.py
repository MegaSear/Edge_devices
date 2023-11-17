class servo():
    def __init__(self):
        self.angle = None
        pass
    def set_angle(self, angle):
        self.angle = angle
        return

class robo_arm():
    def __init__(self, init_angles, list_servos):
        self.current_angles = init_angles
        self.list_servos = list_servos

    def sign(self, a):
        if(a>0): 
            return 1
        if(a<0):
            return -1
        return 0

    def slow_angles(self, new_angles):
        while True:
            step_angles = list(map(self.sign, [x - y for x, y in zip(new_angles, self.current_angles)]))
            self.current_angles = list(map(sum, zip(self.current_angles, step_angles)))
            [servo.set_angle(angle) for servo, angle in zip(self.list_servos, self.current_angles)]
            if step_angles == [0]*len(step_angles):
                break
    
servo1 = servo()
servo2 = servo()
servo3 = servo()
servos = [servo1, servo2, servo3]
init_angles = [90, 90, 90]

robot = robo_arm(init_angles, servos)
#angles_solver()
robot.slow_angles([30, 120, 10])

print(servo1.angle, servo2.angle, servo3.angle)