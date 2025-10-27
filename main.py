"""
This code generates and plots the movement of 1 particle assuming the values as written here.
"""


import random
import math
import numpy as np
import matplotlib.pyplot as plt
from random_generator import gauss_plot
from movement import movement
from configuration import N_movement
from diffusivity import move_diff
from plots import plot_trajectory, plot_configuration, plot_Gamma_Diff, plot_MSD


# -- Dimension, gamma, GAMMA, time_steps, delta_t, Number of particles --

D = 2
gamma = 1
Gamma = 1
time_steps = 100
delta_t = 0.1

flag_1 = True
flag_2 = True
flag_3 = True
flag_4 = True


# -- 2. Generation and plotting of a normal distribution N(0,1) from a uniform distribution for 10000 points --
if flag_1:
    gauss_plot(10000)



# -- 3. 1 Particle Langevin equation using the Eurler-Mayurama algorithm --

if flag_2:
    time_steps = 100
    L = 1
    trajectory = movement(L, 0, D, gamma, Gamma, time_steps, delta_t, False)
    plot_trajectory(trajectory)



# -- 4. Implementation for 1000 particles with Perdiodic boundary conditions -- we divide by %L which is what allows us to know if we are inside or outside, and then we add or deduct -L times this value which will bring us to the right place --

if flag_3:
    N=1000
    L = 100
    delta_t = 0.1 # 0.1 is smaller than 1/(2*Gamma) for Gamma = 1
    
    trajectories = N_movement(N, L, 1, D, gamma, Gamma, time_steps, delta_t, True, True)
    
    
# -- 5. We calculate the mean displacement, and find the diffusivity for a collection of N particles
if flag_4:
    N=1000
    L = 100
    time_steps = 10000
    delta_t = 0.1
    
    Gamma_Diff = []
    MSD = []
    for factor in [0.1, 0.3]:
        results = move_diff(N, L, 1, D, gamma, factor, time_steps, delta_t, False)
        
        for Gamma, Diff, msd in results:
                Gamma_Diff.append({'Gamma': Gamma, 'Diff': Diff})
                MSD.append({'Gamma':Gamma, 'MSD':msd})
    
    
    plot_Gamma_Diff(Gamma_Diff)
    plot_MSD(MSD, delta_t)

    
    
    
    
    
    
    




    

        
    








