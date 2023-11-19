import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def angles_solver(point_1, point_2, L1, L2):
    point_1 = np.array(point_1)
    point_2 = np.array(point_2)
    V = point_2 - point_1
    L3 = np.linalg.norm(V)
    
    if np.any(point_1 < 0):
        print("Point_1 must be in first quadrant!")
    
    if L1 + L2 < L3:
        print("The target point is unreachable (far away)!")
    
    if abs(L1 - L2) > L3:
        print("The target point is unreachable (too close)!")
        
    s1 = 1 #(квадрант)
    cos_beta = (L1**2 + L2**2 - L3**2)/(2*L1*L2)
    beta = np.arccos(cos_beta) if s1 else -np.arccos(cos_beta) #Радианы

    s2 = 1 #(right/left)
    cos_alpha1 = (L1**2 - L2**2 + L3**2)/(2*L1*L3)
    alpha1 = np.arccos(cos_alpha1) if s2 else -np.arccos(cos_alpha1) #Радианы

    n_z = np.array([0, 0, 1])
    cos_alpha2 = np.dot(V, n_z) / (np.linalg.norm(V) * np.linalg.norm(n_z))
    alpha2 = np.pi/2 - np.arccos(cos_alpha2) #Радианы
    
    n_y = np.array([0, 1, 0])
    cos_gamma = np.dot(V, n_y) / (np.linalg.norm(V) * np.linalg.norm(n_y))
    gamma = np.pi/2 - np.arccos(cos_gamma) #Радианы

    alpha = np.radians(np.degrees(alpha1) + np.degrees(alpha2)) #Радианы
    direction_vector = np.array([np.cos(alpha) * np.cos(gamma), np.cos(alpha) * np.sin(gamma), np.sin(alpha)])
    point_3 = point_1 + L1 * direction_vector

    if np.any(point_3 < 0):
        alpha = np.radians(-np.degrees(alpha1) + np.degrees(alpha2))
        direction_vector = np.array([np.cos(alpha) * np.cos(gamma), np.cos(alpha) * np.sin(gamma), np.sin(alpha)])
        point_3 = point_1 + L1 * direction_vector

    #return point_3, 
    alpha = np.degrees(alpha)
    beta = np.degrees(beta)
    gamma = np.degrees(gamma)
    fi1 = 180 - alpha
    fi2 = alpha + beta - 70
    fi3 = gamma
    return fi1, fi2, fi3