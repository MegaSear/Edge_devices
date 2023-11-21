import numpy as np
#import transform3d as t3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R
from Class_Set import char_dict, char_shape

points = char_dict['a']
points_3d = np.array(points)

#Сдвиг каждой точки на вектор
(dx, dy, dz) = (2, 2, 3)
translation_vector = np.array([dx, dy, dz])
points_3d = points_3d + translation_vector

#Поворот в плоскости
rotation_angle = np.radians(0)  # в градусах
rotation_matrix = R.from_euler('x', rotation_angle).as_matrix()
points_3d = np.dot(points_3d, rotation_matrix.T)

#Масштабирование координат
scaling_factor = 1  # коэффициент масштабирования
points_3d  = points_3d * scaling_factor

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Оригинальные точки
ax.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2], label='Исходные точки', marker='o')

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