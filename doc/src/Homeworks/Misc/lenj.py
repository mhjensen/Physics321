import numpy as np
from math import *
import matplotlib.pyplot as plt

#unit conversions of constants

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
