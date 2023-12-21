import numpy as np

def angles_solver(point_2, L1, L2):

    r = 4.7
    dz = 10 #11 8
    n_y = np.array([0, 1, 0])
    n_z = np.array([0, 0, 1])
    n_x = np.array([1, 0, 0])

    a = 0.13 #0.139
    b = -10 #-0.4
    f1 = 10#8.4852813
    radius = np.sqrt(point_2[0]**2 + point_2[1]**2)
    print(point_2)
    point_2 = np.array([point_2[0], point_2[1], 
                        point_2[2] - (np.exp(a*(radius - f1)) + b)])
    print(point_2)
    point_2 = np.array(point_2)
    Vec = point_2

    Vec_cos = np.array([Vec[0], Vec[1], 0])
    gamma = np.arccos(np.dot(Vec_cos, n_y) / (np.linalg.norm(Vec_cos) * np.linalg.norm(n_y)))  #Радианы

    r_vec = np.array([r* np.sin(gamma), r* np.cos(gamma), dz])

    point_1 = np.array(r_vec)

    V = point_2 - point_1
    L3 = np.linalg.norm(V)
    
    if np.any(point_1 < 0):
        print("Point_1 must be in first quadrant!")
    
    if np.any(point_2 < 0):
        print("Point_2 must be in first quadrant!")

    if L1 + L2 < L3:
        print("The target point is unreachable (far away)!")
    
    if L2 - L1 > L3:
        print("The target point is unreachable (too close)!")
        
    s1 = 1 #(квадрант)
    cos_beta = (L1**2 + L2**2 - L3**2)/(2*L1*L2)
    beta = np.arccos(cos_beta) #if s1 else -np.arccos(cos_beta) #Радианы

    s2 = 1 #(right/left)
    cos_alpha1 = (L1**2 - L2**2 + L3**2)/(2*L1*L3)
    alpha1 = np.arccos(cos_alpha1) #if s2 else -np.arccos(cos_alpha1) #Радианы

    cos_alpha2 = np.dot(V, n_z) / (np.linalg.norm(V) * np.linalg.norm(n_z))
    alpha2 = np.pi/2 - np.arccos(cos_alpha2) #Радианы

    alpha = alpha1 + alpha2 #Радианы
    if alpha2 < 0 and alpha1 < abs(alpha2):
        alpha = - (alpha1 + abs(alpha2))

    alpha = np.degrees(alpha)
    beta = np.degrees(beta)
    gamma = np.degrees(gamma)
    fi1 = (180 - alpha) + 22#*(2/3)
    fi2 = (alpha + beta - 70)#*(2/3)
    fi3 = gamma*(2/3)
    return fi1, fi2, fi3