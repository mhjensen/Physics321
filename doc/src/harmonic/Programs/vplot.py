# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt


Deltax = 0.01
#set up arrays
xinitial = -2.0
xfinal = 2.0 
n = ceil((xfinal-xinitial)/Deltax)
x = np.zeros(n)
for i in range(n):
    x[i] = xinitial+i*Deltax
V = np.zeros(n)
# Initial conditions as compact 2-dimensional arrays
alpha = 0.81
beta = 0.5
print(sqrt(alpha/beta))
V = -alpha*x*x*0.5 + beta*(x**4)*0.25
# Plot position as function of time    
fig, ax = plt.subplots()
#ax.set_xlim(0, tfinal)
ax.set_ylabel('x[m]')
ax.set_xlabel('V[s]')
ax.plot(x, V)
fig.tight_layout()
plt.show()




