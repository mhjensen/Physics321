# Exercise 6, hw3, brute force way with declaration of vx, vy, x and y
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

# Output file
outfile = open(data_path("Eulerresults.dat"),'w')

from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'


g = 9.80655 #m/s^2
# The mass and the drag constant D
D = 0.00245 #mass/length   kg/m
m = 0.2 #kg, mass of falling object
DeltaT = 0.01
#set up arrays 
tfinal = 1.4
# set up number of points for all variables
n = ceil(tfinal/DeltaT)
# define scaling constant vT used in analytical solution
vT = sqrt(m*g/D)
# set up arrays for t, a, v, and y and arrays for analytical results
#brute force setting up of arrays for x and y, vx, vy, ax and ay
t = np.zeros(n)
vy = np.zeros(n)
y = np.zeros(n)
vx = np.zeros(n)
x = np.zeros(n)
xanalytic = np.zeros(n)
yanalytic = np.zeros(n)
# Initial conditions
vx[0] = 10.0 #m/s
vy[0] = 0.0  #m/s
y[0] = 10.0 #m
x[0] = 0.0 #m
yanalytic[0] = y[0]
xanalytic[0] = x[0]
# Start integrating using Euler's method
for i in range(n-1):
    # expression for acceleration, note the absolute value and division by mass
    ax = -D*vx[i]*abs(vx[i])/m
    ay = -g - D*vy[i]*abs(vy[i])/m
    # update velocity and position
    x[i+1] = x[i] + DeltaT*vx[i]
    vx[i+1] = vx[i] + DeltaT*ax
    y[i+1] = y[i] + DeltaT*vy[i]
    vy[i+1] = vy[i] + DeltaT*ay
    # update time to next time step and compute analytical answer
    t[i+1] = t[i] + DeltaT
    yanalytic[i+1] = y[0]-(vT*vT/g)*log(cosh(g*t[i+1]/vT))+vy[0]*t[i+1]
    xanalytic[i+1] = log(1.+t[i+1]*vx[0]*D)/D
    if ( y[i+1] < 0.0):
        break
data = {'t[s]': t,
        'Relative error in y': abs((y-yanalytic)/yanalytic),
        'vy[m/s]': vy,
        'Relative error in x': abs((x-xanalytic)/xanalytic),
        'vx[m/s]': vx
}
NewData = pd.DataFrame(data)
display(NewData)
# save to file
NewData.to_csv(outfile, index=False)
#then plot
fig, axs = plt.subplots(4, 1)
axs[0].plot(t, y)
axs[0].set_xlim(0, tfinal)
axs[0].set_ylabel('y')
axs[1].plot(t, vy)
axs[1].set_ylabel('vy[m/s]')
axs[1].set_xlabel('time[s]')
axs[2].plot(t, x)
axs[2].set_xlim(0, tfinal)
axs[2].set_ylabel('x')
axs[3].plot(t, vx)
axs[3].set_ylabel('vx[m/s]')
axs[3].set_xlabel('time[s]')
fig.tight_layout()
save_fig("EulerIntegration")
plt.show()


