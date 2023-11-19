import numpy as np
import transform3d as t3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R

import Class_robotic_tools as rt
import Class_Interpreter as interpreter
from Coords_Transform import angles_solver

class servo():
    def __init__(self):
        self.angle = None
        pass
    def set_angle(self, angle):
        self.angle = angle
        return

num_servo = 3
servos = [servo() for i in range(num_servo)]
init_angles = [90, 90, 90]

robot = rt.Robo_arm(init_angles, servos)
transformer = interpreter.Word_Interpreter()
points = transformer.translate('abc')

start_coords = (0, 5, 0)
L1 = 10
L2 = 9

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = np.array(points)
# Оригинальные точки
ax.scatter(points[:, 0], points[:, 1], points[:, 2], label='Исходные точки', marker='o')

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

# Настройка графика
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.legend()

elev_angle = 25  # угол обзора по оси y
azim_angle = -30  # угол обзора по оси x
ax.view_init(elev=elev_angle, azim=azim_angle)

plt.show()