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

def ForceGravity(v,r,t):
    rabs = np.sqrt(sum(r*r))
    return  -alpha*r/(rabs**3)/m

def PotentialGravity(r):
    return  -alpha/r

def ForceLennardJones(v,r,t):
    return  -alpha*r/(rabs**3)/m

def PotentialLennardJones(r,t):
    return  -alpha*r/(rabs**3)/m


def ForwardEulerCromer(v,r,t,n,Force):
    for i in range(n-1):
        a = Force(v[i],r[i],t[i])
        v[i+1] = v[i] + DeltaT*a
        r[i+1] = r[i] + DeltaT*v[i+1]
        t[i+1] = t[i] + DeltaT

def VelocityVerlet(v,r,t,n,Force):
    for i in range(n-1):
        a = Force(v[i],r[i],t[i])
        r[i+1] = r[i] + DeltaT*v[i]+0.5*a*DeltaT*DeltaT
        anew = Force(v[i],r[i+1],t[i+1])
        v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
        t[i+1] = t[i] + DeltaT


DeltaT = 0.001
#set up arrays 
tfinal = 10  # in years
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,3))
r = np.zeros((n,3))
# define constants
alpha= 4*pi*pi
m = 1.0   # scaled mass of the earth
# Initial conditions as compact 2-dimensional arrays
r0 = np.array([1.0,0.0,0.0])
r[0] = r0
r0abs = np.sqrt(sum(r[0]*r[0]))
# Can easily change to other initial conditions
v0 = np.array([0.0,5.0,0.0])
v[0] = v0
v0abs = np.sqrt(sum(v[0]*v[0]))

# Start integrating using the Velocity-Verlet  method
VelocityVerlet(v,r,t,n,ForceGravity)

# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("Part1Secondmid")
plt.show()


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


sig = 3.405 * 10**(-10) #sigma in meters
m = 39.95 * 1.66*10**(-27) #mass in kilograms
eps = 1.0318*10**(-2) * 1.603*10**(-19) #energy in jules

tau = np.sqrt((sig**2*m)/(eps))
print('Tau is {}'.format(tau))


def Accel(x1,x2):
    a = 24 * (2*abs(x1-x2)**(-12) - abs(x1-x2)**(-6))*(abs(x1-x2)**(-1))
    return a

def VelocityVerlet(v1,v2,x1,x2,t,n,Accel):
    for i in range(n-1):
        a1 = -Accel(x1[i],x2[i])
        a2 = Accel(x1[i],x2[i])
        
        x1[i+1] = x1[i] + dt*v1[i] + 0.5*a1*dt**2
        x2[i+1] = x2[i] + dt*v2[i] + 0.5*a2*dt**2
        
        a1new = -Accel(x1[i+1],x2[i+1])
        a2new = Accel(x2[i+1],x1[i+1])
        
        v1[i+1] = v1[i] + 0.5*dt*(a1+a1new)
        v2[i+1] = v2[i] + 0.5*dt*(a2+a2new)
        
        t[i+1] = t[i] + dt



tfinal = 5 # in years
dt = .01
n = ceil(tfinal/dt)
# set up arrays for position and velocity of atoms
t = np.zeros(n)

x1 = np.zeros(n)
v1 = np.zeros(n)

x2 = np.zeros(n)
v2 = np.zeros(n)

#set initial conditions to center the system at x = 0
sigma = 1 #using this so the scale of the equation can be changed easily 

x1[0] = -(1.5/2)*sigma
v1[0] = 0

x2[0] = (1.5/2) * sigma
v2[0] = 0

VelocityVerlet(v1,v2,x1,x2,t,n,Accel)

distance = x2-x1

plt.figure(figsize = [10,5])

plt.plot(t,distance)
plt.title('Distance Between Atoms Over Time')
plt.xlabel('Time')
plt.ylabel('Distance')

plt.show()

plt.figure(figsize = [10,5])

plt.plot(t,x1,label = 'atom2',color = 'purple')
plt.plot(t,x2,label = 'atom1')
plt.title('Position over time')
plt.xlabel('Time')
plt.ylabel('Position')

plt.legend()
plt.show()


r1 = np.zeros(n)
vel1 = np.zeros(n)

r2 = np.zeros(n)
vel2 = np.zeros(n)

#set initial conditions to center the system at x = 0
sigma = 1 #using this so the scale of the equation can be changed easily 

r1[0] = -(.95/2)*sigma
vel1[0] = 0

r2[0] = (.95/2) * sigma
vel2[0] = 0

VelocityVerlet(vel1,vel2,r1,r2,t,n,Accel)

distance_new = r2-r1

plt.figure(figsize = [10,5])

plt.plot(t,distance_new)
plt.title('Distance Between Atoms Over Time')
plt.xlabel('Time')
plt.ylabel('Distance')

plt.show()

plt.figure(figsize = [10,5])

plt.plot(t,r1,label = 'atom2',color = 'purple')
plt.plot(t,r2,label = 'atom1')
plt.title('Position over time')
plt.xlabel('Time')
plt.ylabel('Position')

plt.legend()
plt.show()


#find the potential energy of the system when they are 1.5 sigma apart
def V(r,eps):
    V = 4*eps*(r**(-12)-r**(-6))
    return V

PE = V(distance,eps)

#find the kinetic energy of the system

KE1 = .5*eps*(v1**2) #this is scaled with r' and t'
KE2 = .5*eps*(v2**2)

KE = KE1+KE2

plt.figure(figsize = [15,10])

plt.subplot(3,1,1)

plt.plot(t,KE)
plt.title('Kinetic Energy - 1.5 sigma')

plt.subplot(3,1,2)

plt.plot(t,PE)
plt.title('Potential Energy - 1.5 sigma')

plt.subplot(3,1,3)

plt.plot(t,PE+KE)
plt.title('Total Energy - 1.5 sigma')
plt.ylim([0,-2e-21])

plt.tight_layout()


#for part 2e
#potential
PE_95 = V(distance_new,eps)

#find the kinetic energy of the system

KE1_95 = .5*eps*(vel1**2) #this is scaled with r' and t'
KE2_95 = .5*eps*(vel2**2)

KE_95 = KE1_95+KE2_95

E_95 = KE_95+PE_95

plt.figure(figsize = [15,10])

plt.subplot(3,1,1)

plt.plot(t,KE_95)
plt.title('Kinetic Energy - .95 sigma')

plt.subplot(3,1,2)

plt.plot(t,PE_95)
plt.title('Potential Energy - .95 sigma')

plt.subplot(3,1,3)

plt.plot(t,E_95)
plt.title('Total Energy - .95 sigma')
plt.ylim([0e-21,5e-21])

plt.tight_layout()
