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

def potential(x):
    return -10.0/x+3.0/x**2+x

def acceleration(x):
    return  -10.0/(x**2)+6.0/(x**3)-1.0
    

from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

DeltaT = 0.0001
#set up arrays 
tfinal = 5.0 # in dimensionless time
n = ceil(tfinal/DeltaT)
# set up arrays for t, v, and x
t = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)
Epot = np.zeros(n)
Ekin = np.zeros(n)
E = np.zeros(n)
eps = np.zeros(n)
# Initial conditions as one-dimensional arrays of time
x0 =  2.0 
v0 = 0.0
x[0] = x0
v[0] = v0
Epot[0] = potential(x0)
Ekin[0] = 0.5*v0**2
E[0] = Epot[0]+Ekin[0]
print(Epot[0],Ekin[0])
# Start integrating using Euler-Cromer's method


for i in range(n-1):
    # Set up the acceleration
    # Here you could have defined your own function for this
    a =  acceleration(x[i])
    # update velocity, time and positio
    x[i+1] = x[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = acceleration(x[i+1])
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)    
    Ekin[i+1] = 0.5*v[i+1]**2
    Epot[i+1] = potential(x[i+1])    
    E[i+1] = Epot[i+1]+Ekin[i+1]
    t[i+1] = t[i] + DeltaT
# Compute abs error in energy
eps = abs(E-E[0])
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_ylabel('x[m]')
ax.set_xlabel('t[s]')
ax.plot(t, E)
fig.tight_layout()
save_fig("ForcedBlockEulerCromer")
plt.show()

