# Exercise 6, hw3, smarter way with declaration of vx, vy, x and y
# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
import os

# Where to save the figures and data files
PROJECT_ROOT_DIR = "Results"
FIGURE_ID = "Results/FigureFiles"
DATA_ID = "DataFiles/"

if not os.path.exists(PROJECT_ROOT_DIR):
    os.mkdir(PROJECT_ROOT_DIR)

if not os.path.exists(FIGURE_ID):
    os.makedirs(FIGURE_ID)

if not os.path.exists(DATA_ID):
    os.makedirs(DATA_ID)

def image_path(fig_id):
    return os.path.join(FIGURE_ID, fig_id)

def data_path(dat_id):
    return os.path.join(DATA_ID, dat_id)

def save_fig(fig_id):
    plt.savefig(image_path(fig_id) + ".png", format='png')


from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

g = 9.80655 #m/s^2
D = 0.0245 #m/s
m = 0.2 # kg
R = 0.1
k = 1000.0
# Define Gravitational force as a vector in x and y
G = -m*g*np.array([0.0,1])
DeltaT = 0.01
#set up arrays 
tfinal = 150.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Initial conditions
r0 = np.array([0.0,2.0])
v0 = np.array([10.0,10.0])
r[0] = r0
v[0] = v0
# Start integrating using Euler's method
for i in range(n-1):
    # Set up forces, air resistance FD
    if ( r[i,1] < R):
        N = k*(R-r[i,1])*np.array([0,1])
    else:
        N = np.array([0,0])
    vabs = sqrt(sum(v[i]*v[i]))
    FD = 0.0#-D*v[i]*vabs
    Fnet = FD+G+N
    a = Fnet/m
    # update velocity, time and position
    v[i+1] = v[i] + DeltaT*a
    r[i+1] = r[i] + DeltaT*v[i+1]
    t[i+1] = t[i] + DeltaT

fig, axs = plt.subplots(2, 1)
axs[0].plot(r[:,0], r[:,1])
axs[0].set_xlim(0, tfinal)
axs[0].set_ylabel('y[m]')
axs[1].plot(t, v[:,1])
axs[1].set_ylabel('vy[m/s]')
axs[1].set_xlabel('x[m]')
fig.tight_layout()
save_fig("YEulerIntegration")
plt.show()


