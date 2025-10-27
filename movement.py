"""
This code generates and plots the movement of 1 particle assuming the values as written here.

Parameters:

    L = Box size
    origin = origin of movement (can be the origin (0,0) or a random point in a box LxL.
    D = Dimension (2D) for the array feneration
    gamma = Langevin equation parameter (damping coefficient)
    Gamma = Langevin equation parameter (noise coefficient)
    time_steps = amount of iterations done 
    delt_t = time added after each time step    
    periodic = if True PBC if False free    
    
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from random_generator import gauss_gen



# -- Makes a 1 particle movement for our function --

def movement(L, origin, D, gamma, Gamma, time_steps, delta_t, periodic):
    trajectory = []
    
    if origin == 0:
        trajectory.append((0,0))
    else:
        x_0 = random.uniform(0,L)
        y_0 = random.uniform(0,L)
        trajectory.append((x_0,y_0))

    for i in range (time_steps):
        x_old, y_old = trajectory[-1]
        
        norm = gauss_gen(D)
        
        x_new = x_old + norm[0]/gamma * np.sqrt(2*Gamma*delta_t)
        y_new = y_old + norm[1]/gamma * np.sqrt(2*Gamma*delta_t)
        
        if periodic:
            # -- Because of python's % operator, it is easier to consider a [0,L] box, since it already shifts our particle to the desired periodic boundary conditions for a LxL box --
            
            x_new = x_new % L
            y_new = y_new % L
            
        trajectory.append((x_new,y_new))
        
    return trajectory






