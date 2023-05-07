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

def ForwardEuler(v,x,t,n,Force):
    for i in range(n-1):
        v[i+1] = v[i] + DeltaT*Force(v[i],x[i],t[i])
        x[i+1] = x[i] + DeltaT*v[i]
        t[i+1] = t[i] + DeltaT


def SpringForce(v,x,t):
#   note here that we have divided by mass and we return the acceleration
    return  -2*nu*v-x+Ftilde*cos(t*Omegatilde)

def ForwardEulerCromer(v,x,t,n,Force):
    for i in range(n-1):
        a = Force(v[i],x[i],t[i])
        v[i+1] = v[i] + DeltaT*a
        x[i+1] = x[i] + DeltaT*v[i+1]
        t[i+1] = t[i] + DeltaT

def VelocityVerlet(v,x,t,n,Force):
    for i in range(n-1):
        a = Force(v[i],x[i],t[i])
        x[i+1] = x[i] + DeltaT*v[i]+0.5*a*DeltaT*DeltaT
        anew = Force(v[i],x[i+1],t[i+1])
        v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
        t[i+1] = t[i] + DeltaT

def RK4(v,x,t,n,Force):
    for i in range(n-1):
# Setting up k1
        k1x = DeltaT*v[i]
        k1v = DeltaT*Force(v[i],x[i],t[i])
# Setting up k2
        vv = v[i]+k1v*0.5
        xx = x[i]+k1x*0.5
        k2x = DeltaT*vv
        k2v = DeltaT*Force(vv,xx,t[i]+DeltaT*0.5)
# Setting up k3
        vv = v[i]+k2v*0.5
        xx = x[i]+k2x*0.5
        k3x = DeltaT*vv
        k3v = DeltaT*Force(vv,xx,t[i]+DeltaT*0.5)
# Setting up k4
        vv = v[i]+k3v
        xx = x[i]+k3x
        k4x = DeltaT*vv
        k4v = DeltaT*Force(vv,xx,t[i]+DeltaT)
# Final result
        x[i+1] = x[i]+(k1x+2*k2x+2*k3x+k4x)/6.
        v[i+1] = v[i]+(k1v+2*k2v+2*k3v+k4v)/6.
        t[i+1] = t[i] + DeltaT

def PendulumForce(v,x,t):
#   note here that we have divided by mass and we return the acceleration
    return  -nu*v-sin(x)+Ftilde*cos(t*Omegatilde)

DeltaT = 0.0001
#set up arrays 
tfinal = 10
n = ceil(tfinal/DeltaT)
# set up arrays for t, v, and x
t = np.zeros(n)
v = np.zeros(n)
#Energy = np.zeros(n)
theta = np.zeros(n)
# Initial conditions
# Note that the equation has been scaled so that mass, g etc are baked into scaled constants
theta0 =  0.2
v0 = 0.0
theta[0] = theta0
v[0] = v0
nu = 0.0
Omegatilde = 0.0
Ftilde = 0.0
# Start integrating using the RK4 method
# Note that we define the force function via the function  PendulumForce
RK4(v,theta,t,n,PendulumForce)
# Then compute total energy, vectorized version
Energy = 0.5*v*v-np.cos(theta)
KineticEnergy = 0.5*v*v
PotentialEnergy = -np.cos(theta)
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_ylabel('Total Energy')
ax.set_xlabel('t[s]')
ax.plot(t, Energy)
ax.plot(t, KineticEnergy)
ax.plot(t, PotentialEnergy)
fig.tight_layout()
plt.show()
