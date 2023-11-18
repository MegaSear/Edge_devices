import numpy as np

def helper(point_1, point_2, L1, L2):

    L3 = np.linalg.norm(point_2 - point_1)
    if L1 + L2 < L3:
        print("L1 + L2 <= L3!")
    
    if abs(L1 - L2) > L3:
        print("L1 - L2 > L3!")

    cos_beta = (L1**2 + L2**2 - L3**2) / (2 * L1 * L2)
    beta = np.arccos(np.clip(cos_beta, -1, 1))

    tg_alpha2 = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
    alpha2 = np.arctan2(point_2[1] - point_1[1], point_2[0] - point_1[0])

    alpha1 = np.arccos((L1**2 - L2**2 + L3**2) / (2 * L1 * L3))
    alpha = alpha1 + alpha2 

    # Расчет углов beta и gamma
    gamma = np.arctan2(np.linalg.norm(point_2[:2] - point_1[:2]), point_2[2] - point_1[2])
    beta = np.pi - beta  # Переворачиваем угол beta
    
    return np.degrees(alpha), np.degrees(beta), np.degrees(gamma)

def angles_solver(point_1, point_2, L1, L2):
    # Расчет углов
    point_2 = np.array(point_2)
    point_1 = np.array(point_1)
    alpha, beta, gamma = helper(point_1, point_2, L1, L2)

    # Расчет координат промежуточной точки
    point_3 = np.array([point_1[0] + L1 * np.cos(np.radians(alpha)),
                        point_1[1] + L1 * np.sin(np.radians(alpha)),
                        point_1[2]])

    return point_3, alpha, beta, gamma