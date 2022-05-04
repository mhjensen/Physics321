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

def ForceLennardJones(r1,r2):
    r = np.sqrt(sum((r1-r2)**2))
    return  24*(2.0*r**(-14)-r**(-8))*(r1-r2)

def PotentialLennardJones(r1,r2):
    r = np.sqrt(sum((r1-r2)**2))    
    return  4*(r**(-12)-r**(-6))


def VelocityVerlet(v1,r1,v2,r2,t,n,Force):
    for i in range(n-1):
        a1 = Force(r1[i],r2[i])
        a2 = -a1
        r1[i+1] = r1[i] + DeltaT*v1[i]+0.5*a1*DeltaT*DeltaT
        r2[i+1] = r2[i] + DeltaT*v2[i]+0.5*a2*DeltaT*DeltaT        
        a1new = Force(r1[i+1],r2[i+1])
        a2new = -a1new
        v1[i+1] = v1[i] + 0.5*DeltaT*(a1+a1new)
        v2[i+1] = v2[i] + 0.5*DeltaT*(a2+a2new)
        t[i+1] = t[i] + DeltaT


DeltaT = 0.001
#set up arrays 
tfinal = 10 
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v1 = np.zeros((n,3))
r1 = np.zeros((n,3))
r2 = np.zeros((n,3))
v2 = np.zeros((n,3))

# Initial conditions as compact 2-dimensional arrays
r10 = np.array([1.0,0.0,0.0])
r1[0] = r10
r20 = np.array([0.0,1.0,0.0])
r2[0] = r20
# Can easily change to other initial conditions
v10 = np.array([0.0,0.0,0.0])
v1[0] = v10
v20 = np.array([0.0,0.0,0.0])
v2[0] = v20

# Start integrating using the Velocity-Verlet  method
VelocityVerlet(v1,r1,v2,r2,t,n,ForceLennardJones)
r = np.zeros(n)
r = np.sqrt(sum((r1-r2)**2))
print(r)
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_xlabel('t')
ax.set_ylabel('r')
#ax.plot(t, r)
fig.tight_layout()
save_fig("Positions")
plt.show()

"""
# Using the solutions for r and v we can now calculate the energies
Ekin = np.zeros(n)
Vpot = np.zeros(n)
ETotal = np.zeros(n)
# Use r and v to set up the energies
for i in range(n):
    rabs = np.sqrt(sum(r[i]*r[i]))
    vabs = np.sqrt(sum(v[i]*v[i]))
    Ekin[i] = 0.5*m*vabs*vabs
    Vpot[i] = PotentialGravity(rabs)
    ETotal[i] = Ekin[i]+Vpot[i]

fig, ax = plt.subplots()
ax.set_xlabel('t')
ax.set_ylabel('E')
ax.plot(t, ETotal)
ax.plot(t, Ekin)
ax.plot(t, Vpot)
fig.tight_layout()
save_fig("Final")
plt.show()
"""

