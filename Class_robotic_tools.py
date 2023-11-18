class Robo_arm():
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
            #Получим список единичных векторов направлений движения (углов) для каждой servo
            #Исходя из текущего угла и целевого
            step_angles = list(map(self.sign, [x - y for x, y in zip(new_angles, self.current_angles)]))

            #Этот список текущих углов отправим на каждую servo
            self.current_angles = list(map(sum, zip(self.current_angles, step_angles)))
            [servo.set_angle(angle) for servo, angle in zip(self.list_servos, self.current_angles)]

            #Заканчиваем поворот servos в случае если единичные вектора направлений все равны нулю
            #То есть разница между current и target равна нулю
            if step_angles == [0]*len(step_angles):
                break