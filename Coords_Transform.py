import numpy as np

def angles_solver(x0, y0, x2, y2, L1, L2):
    #Принимает на вход две точки и длины локтей!!!
    
    L3 = np.sqrt((x2-x0)**2 + (y2-y0)**2)
    
    if x0 < 0 or y0 < 0:
        print("x0 < 0 or y0 < 0!")
    
    if L1 + L2 <= L3:
        print("L1 + L2 <= L3!")
    
    if abs(L1 - L2) > L3:
        print("L1 - L2 > L3!")
        
    s1 = 1 #(квадрант)
    cos_beta = (L1**2 + L2**2 - L3**2)/(2*L1*L2)
    beta = np.arccos(cos_beta) if s1 else -np.arccos(cos_beta) 

    s2 = 1 #(right/left)
    cos_alpha1 = (L1**2 - L2**2 + L3**2)/(2*L1*L3)
    alpha1 = np.arccos(cos_alpha1)  if s2 else -np.arccos(cos_alpha1) 

    tg_alpha2 = (y2-y0)/(x2-x0)
    alpha2 = np.arctan(tg_alpha2)
    
    alpha = alpha1 + alpha2
    x1 = x0 + L1 * np.cos(alpha)
    y1 = y0 + L1 * np.sin(alpha)

    if x1<0 or y1<0:
        alpha = -alpha1 + alpha2
        x1 = x0 + L1 * np.cos(alpha)
        y1 = y0 + L1 * np.sin(alpha)
    return x1, y1, alpha, beta