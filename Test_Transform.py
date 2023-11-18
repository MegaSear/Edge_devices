import numpy as np
import transform3d as t3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R
from Class_Set import char_dict, char_shape

points = char_dict['a']
points_3d = np.array(points)

#Сдвиг каждой точки на вектор
(dx, dy, dz) = (5, 5, 1)
translation_vector = np.array([dx, dy, dz])
translated_points = points_3d + translation_vector

#Поворот в плоскости
rotation_angle = np.radians(30)  # в градусах
rotation_matrix = R.from_euler('x', rotation_angle).as_matrix()
rotated_points = np.dot(points_3d, rotation_matrix.T)

#Масштабирование координат
scaling_factor = 2  # коэффициент масштабирования
scaled_points = points_3d * scaling_factor

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Оригинальные точки
ax.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2], label='Исходные точки', marker='o')
ax.scatter(translated_points[:, 0], translated_points[:, 1], translated_points[:, 2], label='Сдвиг', marker='^')
ax.scatter(rotated_points[:, 0], rotated_points[:, 1], rotated_points[:, 2], label='Поворот', marker='s')
ax.scatter(scaled_points[:, 0], scaled_points[:, 1], scaled_points[:, 2], label='Масштаб', marker='*')

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