import numpy as np
import transform3d as t3d
from Set_Char3D import char_dict, char_shape

class Word_Interpreter():
    def __init__(self):
        self.dict = char_dict
        self.word = []
        self.char_shape = char_shape
        return
    
    def transform(points_3d):
        points_3d = np.array(points_3d)

        #Сдвиг каждой точки на вектор
        (dx, dy, dz) = (5, 5, 0)
        translation_vector = np.array([dx, dy, dz])
        translated_points = points_3d + translation_vector

        #Поворот в плоскости
        rotation_angle = np.radians(0)  # в градусах
        rotation_matrix = t3d.axangles.axangle2mat((0, 0, 1), rotation_angle)
        translated_points = np.dot(translated_points, rotation_matrix.T)

        #Масштабирование координат
        scaling_factor = 1.5  # коэффициент масштабирования
        translated_points = translated_points * scaling_factor

        return translated_points
    
    def translate(self, word):
        self.word = list(word)
        translation = []
        offset_z = 2
        offset_x = self.char_shape[0]

        for i, char in enumerate(self.word):

            #получение 3d точек из словаря по символу
            points_3d = self.dict[char]
            #добавим новую точку после прорисовки слова - точку отрыва от рисования
            new_point = (points_3d[-1][0], points_3d[-1][1], points_3d[-1][2] + offset_z)
            points_3d.append(new_point)

            #Шифтанём прорисовывающийся символ на количество уже написанных символов
            shifted_points_3d = [(x + i*offset_x, y, z) for x, y, z in points_3d]

            #Исходя из известных данных о положении плоскости рисования и модели roboarm трансформируем координаты
            #Добавим последовательность точек в итоговый список точек
            translation += self.transform(shifted_points_3d)
            
        return translation
