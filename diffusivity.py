"""
This code generates and finds the diffusivity for a collection of N particles. It returns this value and then plots it in a log-log scale
       
"""

import numpy as np
from configuration import N_movement


# -- Makes a N particle movement  --
def move_diff(N, L, origin, D, gamma, factor, time_steps, delta_t, periodic):
    
    Diff_Gamma = []

    # -- how many Gamma powers we want is the value inside range() --
    for i in range (5):
        Gamma = factor*(10**i)
        trajectories = N_movement(N, L, origin, D, gamma, Gamma, time_steps, delta_t, periodic, False)
        msd=msd_calculation(trajectories, time_steps)
        
        Diff = diffusivity_calculation(trajectories, time_steps*delta_t)
        Diff_Gamma.append((Gamma,Diff,msd))

    return Diff_Gamma

# -- computes msd for each time_step for a set of trajectories --
def msd_calculation(trajectories, time_steps):
    
    trajectories = np.array(trajectories)
    
    msd = np.zeros(time_steps+1)
    for t in range(time_steps + 1):

        dx1 = (trajectories[:, t, 0] - trajectories[:, 0, 0])**2
        dx2 = (trajectories[:, t, 1] - trajectories[:, 0, 1])**2

        msd[t] = np.mean(dx1+dx2)

    return msd


# -- computes D for a set of trajectories --
def diffusivity_calculation(trajectories, time):

    MSD = 0.0
    for traj in trajectories:
        traj = np.array(traj)
        dr = traj[-1] - traj[0]
        MSD += np.sum(dr**2)
             
    MSD /= len(trajectories)
    Diff = MSD/(4*time)
    
    return Diff



