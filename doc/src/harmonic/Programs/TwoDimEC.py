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

DeltaT = 0.001
#set up arrays 
tfinal = 20.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Setting up parameters for the model
d = 0.1
mass = 1.0
V0 = 1.0
c1 = 4*V0/(d**4)/mass
c2 = 4*V0/(d**2)/mass
gamma = 0.1
# Initial conditions as compact 2-dimensional arrays, here r =(d,0) and v =(0,0.5)
r0 = np.array([d,0.0])
v0 = np.array([0.0,0.5])
r[0] = r0
v[0] = v0
# Start integrating using the Euler-Cromer method
for i in range(n-1):
    # Set up the acceleration, need the absolute value of r first
    rabs = sqrt(sum(r[i]*r[i]))
    a =  (c2*rabs-c1*(rabs**3))*r[i]/rabs
    # update velocity, time and position using the Euler-Cromer method
    v[i+1] = v[i] + DeltaT*a
    r[i+1] = r[i] + DeltaT*v[i+1]
    t[i+1] = t[i] + DeltaT
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_ylabel('x[m]')
ax.set_xlabel('y[m]')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("TwodimEulerCromer")
plt.show()
