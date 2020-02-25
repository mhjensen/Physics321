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
tfinal = 1.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v, and x
t = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)
E = np.zeros(n)
alpha = 0.81
beta = 1.0
mass = 1.0
# Initial conditions as compact 2-dimensional arrays
x0 =  sqrt(alpha/beta)
v0 = 0.5
x[0] = x0
v[0] = v0
E[0] = 0.5*mass*v0*v0
# Start integrating using Euler's method
for i in range(n-1):
    a =  -alpha*x[i]/mass+beta*(x[i]**3)/mass
    # update velocity, time and position using Euler's forward method
    v[i+1] = v[i] + DeltaT*a
    x[i+1] = x[i] + DeltaT*v[i+1]
#    E[i+1] = 0.5*mass*v[i+1]*v[i+1]+
    t[i+1] = t[i] + DeltaT
# Plot position as function of time    
fig, ax = plt.subplots()
#ax.set_xlim(0, tfinal)
ax.set_ylabel('v[m/s]')
ax.set_xlabel('x[m]')
#ax.plot(t, x)
ax.plot(x, v)
fig.tight_layout()
save_fig("BlockEulerCromer")
plt.show()




