"""
Main of our project. each flag is one exercise:
flag_ex2: generates N(0,1) numbers from U(0,1)
flag_ex3: simulates a 1 particle movement with or without PBC
flag_ex4: simulates an N particle configuration with or without PBC
flag_ex5: finds the msd and D of a configuration with N particles with no PBC
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


# -- Dimension (2D), gamma (damping), Gamma (noise), time_steps, delta_t. We will also encounter N = number of particles, L = size of LxL box --

D = 2
gamma = 1
Gamma = 1
time_steps = 100
delta_t = 0.1

flag_ex2 = True
flag_ex3 = True
flag_ex4 = True
flag_ex5 = True


# -- 2. Generation and plotting of a normal distribution N(0,1) from a uniform distribution for 10000 points --
if flag_ex2:
    gauss_plot(10000)



# -- 3. 1 Particle Langevin equation using the Eurler-Mayurama algorithm --

if flag_ex3:
    time_steps = 100
    L = 1
    trajectory = movement(L, 0, D, gamma, Gamma, time_steps, delta_t, False)
    plot_trajectory(trajectory)



# -- 4. Implementation for 1000 particles with Perdiodic boundary conditions -- we divide by %L which is what allows us to know if we are inside or outside, and then we add or deduct -L times this value which will bring us to the right place --

if flag_ex4:
    N=1000
    L = 100
    
    trajectories = N_movement(N, L, 1, D, gamma, Gamma, time_steps, delta_t, True, True)
    
    
# -- 5. We calculate the mean displacement, and find the diffusivity for a collection of N particles
if flag_ex5:
    N=1000
    L = 100
    time_steps = 10000
    
    Gamma_Diff = []
    MSD = []
    for factor in [0.1, 0.3]:
        results = move_diff(N, L, 1, D, gamma, factor, time_steps, delta_t, False)
        
        for Gamma, Diff, msd in results:
                Gamma_Diff.append({'Gamma': Gamma, 'Diff': Diff})
                MSD.append({'Gamma':Gamma, 'MSD':msd})
    
    
    plot_Gamma_Diff(Gamma_Diff)
    plot_MSD(MSD, delta_t)

    
    
    
    
    
    
    




    

        
    








