"""
This code generates and plots the movement of N particles. The plot flag indicates if we want to plot the initial and final configuration states and a particles movement.
       
"""

from movement import movement
from plots import plot_configuration, plot_trajectory

# -- Simulates the movement for N particles --

def N_movement(N, L, origin, D, gamma, Gamma, time_steps, delta_t, periodic, plot):
    trajectories = []

    for i in range(N):
        traj = movement(L, origin , D, gamma, Gamma, time_steps, delta_t, periodic)
        trajectories.append(traj)

    # -- plot the initial and final configurations --
    if plot:
        x0 = [traj[0][0] for traj in trajectories]
        y0 = [traj[0][1] for traj in trajectories]
        
        xend = [traj[-1][0] for traj in trajectories]
        yend = [traj[-1][1] for traj in trajectories]
        
        plot_configuration(x0, y0, xend, yend, "Particle configuration", "../Plots/ini_fin_config.png")
        plot_trajectory(trajectories[2])
        
    return trajectories






