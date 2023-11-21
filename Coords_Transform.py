import numpy as np

def angles_solver(point_1, point_2, L1, L2):

    o = np.array([0, 0, 0])
    r = 5
    dz = 6
    n_y = np.array([0, 1, 0])
    n_z = np.array([0, 0, 1])
    n_x = np.array([1, 0, 0])

    Vec = point_2 - o
    teta = np.pi/2 - np.arccos(np.dot(Vec, n_z) / (np.linalg.norm(Vec) * np.linalg.norm(n_z)))

    Vec_cos = Vec*np.cos(teta)
    cos_gamma = np.dot(Vec_cos, n_y) / (np.linalg.norm(Vec_cos) * np.linalg.norm(n_y))
    gamma = np.arccos(cos_gamma) #Радианы

    r_vec = np.array([r*np.cos(gamma), r*np.sin(gamma), dz])

    point_1 += r_vec

    point_1 = np.array(point_1)
    point_2 = np.array(point_2)
    V = point_2 - point_1
    L3 = np.linalg.norm(V)
    
    if np.any(point_1 < 0):
        print("Point_1 must be in first quadrant!")
    
    if np.any(point_2 < 0):
        print("Point_2 must be in first quadrant!")

    if L1 + L2 < L3:
        print("The target point is unreachable (far away)!")
    
    if L1 - L2 > L3:
        print("The target point is unreachable (too close)!")
        
    s1 = 1 #(квадрант)
    cos_beta = (L1**2 + L2**2 - L3**2)/(2*L1*L2)
    beta = np.arccos(cos_beta) #if s1 else -np.arccos(cos_beta) #Радианы

    s2 = 1 #(right/left)
    cos_alpha1 = (L1**2 - L2**2 + L3**2)/(2*L1*L3)
    alpha1 = np.arccos(cos_alpha1) #if s2 else -np.arccos(cos_alpha1) #Радианы

    cos_alpha2 = np.dot(V, n_z) / (np.linalg.norm(V) * np.linalg.norm(n_z))
    alpha2 = np.pi/2 - np.arccos(cos_alpha2) #Радианы
    
    #n_y = np.array([0, 1, 0])
    #V_cos = V*np.cos(alpha2)
    #cos_gamma = np.dot(V, n_y) / (np.linalg.norm(V_cos) * np.linalg.norm(n_y))
    #gamma = np.arccos(cos_gamma) #Радианы

    alpha = alpha1 + alpha2 #Радианы
    if alpha2 < 0 and alpha1 < abs(alpha2):
        alpha = - (alpha1 + abs(alpha2))

    direction_vector = np.array([np.cos(alpha) * np.cos(gamma), np.cos(alpha) * np.sin(gamma), np.sin(alpha)])
    point_3 = point_1 + L1 * direction_vector

    #return point_3, 
    alpha = np.degrees(alpha)
    beta = np.degrees(beta)
    gamma = np.degrees(gamma)
    fi1 = (180 - alpha)#*(2/3)
    fi2 = (alpha + beta - 70)#*(2/3)
    fi3 = gamma*(2/3)
    return fi1, fi2, fi3