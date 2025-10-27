"""
This code plots different things.
"""

import numpy as np
import matplotlib.pyplot as plt


# -- Plots a system state at a given time --
def plot_configuration(x0,y0, xend, yend, title,name):
    plt.figure(figsize=(6,6))
    plt.scatter(x0, y0, s=3, c='blue')
    plt.scatter(xend, yend, s=3, c='red')
    plt.title(f"{title}")
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(f"{name}")
    plt.close()
    
# -- Plots the trajectory of a particle --
def plot_trajectory(trajectory):
    # -- plot trajectory --
    x, y = zip(*trajectory)
    plt.plot(x, y, 'b-o')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Trajectory Equations")
    plt.savefig("../Plots/Trajectory_1_particle.png")
    plt.close()

# -- Plots the Diffusivity vs Gamma in log-log scale
def plot_Gamma_Diff(Gamma_Diff):
    Gamma = [d['Gamma'] for d in Gamma_Diff]
    Diff = [d['Diff'] for d in Gamma_Diff]

    plt.figure(figsize=(6,6))
    gamma_line = np.linspace(min(Gamma), max(Gamma), 1000)
    plt.loglog(gamma_line, gamma_line, 'r--', label=r'$D = \Gamma$')
    plt.loglog(Gamma, Diff, marker='X', markersize=5, linestyle='')
    plt.xlabel(r'$\Gamma$')
    plt.ylabel(r'$D$')
    plt.title("Diffusivity vs Gamma")
    plt.grid(True, which='both', ls='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("../Plots/Diff_vs_Gamma.png")
    plt.close()

def plot_MSD(MSD,delta_t):
    # Create a time array (in physical units if you want)
    time = np.arange(len(MSD[0]['MSD'])) * delta_t

    plt.figure(figsize=(8,6))

    for entry in MSD:
        Gamma = entry['Gamma']
        msd = entry['MSD']
        plt.plot(time, msd, label=f'Γ = {Gamma:.2e}')

    plt.xlabel('Time')
    plt.ylabel('Mean Squared Displacement (MSD)')
    plt.ylim(0,10000)
    plt.title('MSD vs Time for Different Γ')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Plots/MSD_vs_time.png")
    plt.close()
    
    
    plt.figure(figsize=(8,6))
    for entry in MSD:
        Gamma = entry['Gamma']
        msd = entry['MSD']
        plt.plot(time, msd, label=f'Γ = {Gamma:.2e}')

    plt.xlabel('Time')
    plt.ylabel('Mean Squared Displacement (MSD)')
    plt.title('MSD vs Time for Different Γ')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../Plots/MSD_vs_time_total.png")
    plt.close()

