# Exercise 7, hw3, smarter way with declaration of vx, vy, x and y
# Here we have added a normal force from the ground
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

# Define constants
g = 9.80655 #in m/s^2
D = 0.0245 # in mass/length, kg/m
m = 0.2 # in kg
R = 0.1 # in meters
k = 1000.0 # in mass/time^2
# Define Gravitational force as a vector in x and y, zero x component
G = -m*g*np.array([0.0,1])
DeltaT = 0.01
#set up arrays 
tfinal = 15.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v, and r, the latter contain the x and y comps
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
    FD = -D*v[i]*vabs
    Fnet = FD+G+N
    a = Fnet/m
    # update velocity, time and position
    v[i+1] = v[i] + DeltaT*a
    r[i+1] = r[i] + DeltaT*v[i+1]
    t[i+1] = t[i] + DeltaT

fig, ax = plt.subplots()
ax.set_xlim(0, tfinal)
ax.set_ylabel('y[m]')
ax.set_xlabel('x[m]')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("BouncingBallEuler")
plt.show()




