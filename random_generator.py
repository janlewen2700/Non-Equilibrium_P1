"""
This code generates and plots the distribution of a random N(0,1) sample based on an uniform generator. It uses random.random() a built-in function in the random package that uses the Marsene Twister algorithm to generate random numbers in with a uniform (0,1) distribution.

We implement the Box-Muller algorithm to modify the values into a N(0,1) distribution.
"""


import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as norm_dist



def gauss_plot(N):
    norm = []

    for i in range(N//2):
        u1 = random.random()
        u2 = random.random()
        
        z1 = math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2)
        z2 = math.sqrt(-2*math.log(u2))*math.cos(2*math.pi*u1)
        
        norm.append(z1)
        norm.append(z2)

    norm=np.array(norm)

    # -- we calculate mean and variance --
    mean = np.mean(norm)
    variance = np.var(norm)
    std_dev = np.sqrt(variance)

    print("mean: ", mean, "variance: ", variance, "\n")



    # -- we plot the values --
    plt.figure(figsize=(6, 5))
    plt.hist(norm, bins=100, density=True, alpha=0.6)
    plt.title("Gaussian Distribution (Box–Muller Transform) [log scale]")
    plt.axvline(mean, color='k', linestyle='--', linewidth=1.5, label=f'Mean')
    plt.axvline(mean - std_dev, color='g', linestyle=':', linewidth=1.2, label=f'-1σ')
    plt.axvline(mean + std_dev, color='g', linestyle=':', linewidth=1.2, label=f'+1σ')
    plt.xscale("linear")
    plt.yscale("log")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.xlim(-4,4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../Plots/G_dist_log.png")
    plt.close()
    
    # --- Linear plot with theoretical N(0,1) overlay ---
    plt.figure(figsize=(6, 5))
    plt.hist(norm, bins=100, density=True, alpha=0.6)

    # Theoretical N(0,1) curve
    x = np.linspace(min(norm), max(norm), 500)
    plt.plot(x, norm_dist.pdf(x, 0, 1), 'r-', lw=2, label=r'$\mathcal{N}(0,1)$')

    plt.title("Gaussian Distribution (Box–Muller Transform) [linear scale]")
    plt.axvline(mean, color='k', linestyle='--', linewidth=1.5, label='Mean')
    plt.axvline(mean - std_dev, color='g', linestyle=':', linewidth=1.2, label=f'-1σ')
    plt.axvline(mean + std_dev, color='g', linestyle=':', linewidth=1.2, label=f'+1σ')
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.xlim(-4,4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../Plots/G_dist_linear.png")
    plt.close()
    



def gauss_gen(N):
    norm=[]
    for i in range(N//2):
        u1 = random.random()
        u2 = random.random()
        
        z1 = math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2)
        z2 = math.sqrt(-2*math.log(u2))*math.cos(2*math.pi*u1)
        
        norm.append(z1)
        norm.append(z2)

    norm=np.array(norm)
    return norm





