# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt


Deltax = 0.01
#set up arrays
xinitial = -5.0
xfinal = 5.0 
n = ceil((xfinal-xinitial)/Deltax)
x = np.zeros(n)
for i in range(n):
    x[i] = xinitial+i*Deltax
V = np.zeros(n)
# Initial conditions as compact 2-dimensional arrays
alpha = 10.0
beta = 2.0
d = 1.0; v0= 0.1;
V = v0*((x**2-d**2)**2)/(d**4)
# Plot position as function of time    
fig, ax = plt.subplots()
#ax.set_xlim(0, tfinal)
ax.set_ylabel('x[m]')
ax.set_xlabel('V[s]')
ax.plot(x, V)
fig.tight_layout()
plt.show()




