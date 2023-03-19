import numpy as np
from math import *
import matplotlib.pyplot as plt


# The acceleration a = F/m  with F = -dV/dx
def acceleration(x):
    return (-1/m)*((10/(x**2)) + (-2*3/(x**3)) + 1)
def potential_energy(x):
    return -10.0/x +3.0/(x**2) + 1.0*x
# initial time
t0 = 0
#final time
tf = 10.0
dt = 0.00001
# set up array for time steps
t = np.arange(t0,tf+dt,dt)
# mass and potential parameters part 2
m = 1.0
V0 = 0.1
d = 0.1
# initial values
v0 = 0.0
x0 = 2.0
x = np.zeros(len(t))
v = np.zeros(len(t))
v[0] = v0
x[0] = x0
# integrate v and x
for i in range(len(t)-1):
    a_i = acceleration(x[i])
    x[i+1] = x[i] + dt*v[i] + 0.5*a_i*(dt**2)
    a_ip1 = acceleration(x[i+1])
    v[i+1] = v[i] + 0.5*dt*(a_i + a_ip1)
plt.plot(t,x)
plt.show()


# now use the arrays of x and v to test energy conservation
# define potential, kinetic and total energies
Ekin = np.zeros(len(t))
Epot = np.zeros(len(t))
Etot = np.zeros(len(t))
Ekin[0] = 0.5*v0*v0/m
Epot[0] = potential_energy(x0)
Etot[0] = Ekin[0]+Epot[0]
ekin = epot =0.0
# set up total energy as function of time
for i in range(1,len(t)):
    ekin = 0.5*v[i]*v[i]/m
    Ekin[i] += ekin
    epot = potential_energy(x[i])
    Epot[i] += epot
    Etot[i] += ekin+epot
plt.plot(t,Etot)
plt.show()

