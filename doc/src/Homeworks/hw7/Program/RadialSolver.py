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

DeltaT = 0.01
#set up arrays 
tfinal = 10.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v and r
t = np.zeros(n)
v = np.zeros(n)
r = np.zeros(n)
# Constants of the model
k = 0.1   # spring constant
m = 0.1   # mass, you can change these
omega02 = k/m  # Frequency
AngMom = 1.0  #  The angular momentum
c = AngMom*AngMom/(m*m)
# Initial conditions
r0 = (AngMom*AngMom/k/m)**0.25
v0 = 0.0
r[0] = r0
v[0] = v0

# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up forces, define rabs first
    a =  -r[i]*omega02+c/(r[i]**3)  # you may need to change this
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -r[i+1]*omega02+c/(r[i+1]**3)  
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
# Plot position as function of time
fig, ax = plt.subplots()
ax.set_xlabel('t[s]')
ax.set_ylabel('r[m]')
ax.plot(t,r)
fig.tight_layout()
save_fig("RadialHOVV")
plt.show()
