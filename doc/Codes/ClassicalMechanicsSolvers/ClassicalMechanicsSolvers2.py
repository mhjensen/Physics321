# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
import os

def freefall_acceleration (params):
    g,D,v,x,t = params
    return -g + D*v*v

def freefall_yanalytic (params):
    g,D,y_0,v_0,v,x,t = params
    vT = sqrt(g/D)
    return y_0-(vT*vT/g)*log(cosh(g*t/vT))

def freefall_no_drag_acceleration  (params): #Arguments must be in the same order
    g,D,v,x,t = params
    return -g

def freefall_no_drag_yanalytic (params):
    g,D,y_0,v_0,v,x,t = params
    return -0.5*g*t**2 + v_0*t + y_0    

def twoD_HO_acceleration(params):
    omega_squared, v, x, t
    return -x*omega_squared


class ClassicalMechanicsSolvers ():
    def __init__(self, params_a, params_y, DeltaT, tfinal, v_0, y_0, m=1, oneD = True):
        self.m = m
        self.params_a = params_a
        self.params_y = params_y
        self.set_up_time (DeltaT, tfinal)
        if oneD:
            self.set_up_initial_arrays_1D (v_0, y_0)
        else:
            self.set_up_initial_arrays_2D (v_0, y_0)
        
    ###############################################
    # SETTING UP TIME
    def set_up_time (self, DeltaT, tfinal):
        self.DeltaT = DeltaT
        self.n = ceil(tfinal/DeltaT)
        self.t = np.zeros(self.n)
    ###############################################

    ###############################################
    # SETTING UP THE INITIAL ARRAYS
    def set_up_initial_arrays_1D (self, v_0, y_0): ## No longer need n as an argument
        # set up arrays for t, a, v, and y and we can compare our results with analytical ones
        self.a = np.zeros(self.n)
        self.v = np.zeros(self.n)
        self.y = np.zeros(self.n)
        self.yanalytic = np.zeros(self.n)
        # Initial conditions
        self.v[0] = v_0  #m/s
        self.y[0] = y_0 #m
        self.yanalytic[0] = self.y[0]
    ###############################################
    
    ###############################################
    # SETTING UP THE INITIAL ARRAYS
    def set_up_initial_arrays_2D (self, v_0, y_0): ## No longer need n as an argument
        # set up arrays for t, a, v, and y and we can compare our results with analytical ones
        self.a = np.zeros((self.n,2))
        self.v = np.zeros((self.n,2))
        self.y = np.zeros((self.n,2))
        self.yanalytic = np.zeros((self.n,2))
        # Initial conditions
        self.v[0] = v_0  #m/s
        self.y[0] = y_0 #m
        self.yanalytic[0] = self.y[0]
    ###############################################

    ###############################################
    # EULER'S METHOD
    def euler (self, min_position, acceleration_eq, yanalytic_eq):
        stop_i = self.n
        # Start integrating using Euler's method
        for i in range(self.n-1):
            # expression for acceleration
            params_a = np.concatenate((self.params_a, [self.v[i], self.y[i], self.t[i]]))
            self.a[i] = acceleration_eq (params_a) 
            # update velocity and position
            self.y[i+1] = self.y[i] + self.DeltaT*self.v[i]
            self.v[i+1] = self.v[i] + self.DeltaT*self.a[i]
            # update time to next time step and compute analytical answer
            self.t[i+1] = self.t[i] + self.DeltaT
            params_y = np.concatenate((self.params_y, [self.v[i], self.y[i], self.t[i]]))
            self.yanalytic[i+1] = yanalytic_eq(params_y) 
            if ( self.y[i+1] < min_position):
                stop_i = i+2
                break
        if stop_i != self.n:
            self.t = self.t[0:stop_i]
            self.a = self.a[0:stop_i]
            self.v = self.v[0:stop_i]
            self.y = self.y[0:stop_i]
            self.yanalytic = self.yanalytic[0:stop_i]
        params_a = np.concatenate((self.params_a, [self.v[-1], self.y[-1], self.t[-1]]))
        self.a[-1] = acceleration_eq (params_a) 
    ###############################################
    
    ###############################################
    # EULER-CROMER METHOD
    def euler_cromer (self, min_position, acceleration_eq, yanalytic_eq):
        stop_i = self.n
        # Start integrating using Euler's method
        for i in range(self.n-1):
            # expression for acceleration
            params_a = np.concatenate((self.params_a, [self.v[i], self.y[i], self.t[i]]))
            self.a[i] = acceleration_eq (params_a) 
            # update velocity and position
            self.v[i+1] = self.v[i] + self.DeltaT*self.a[i]
            self.y[i+1] = self.y[i] + self.DeltaT*self.v[i+1]
            # update time to next time step and compute analytical answer
            self.t[i+1] = self.t[i] + self.DeltaT
            params_y = np.concatenate((self.params_y, [self.v[i], self.y[i], self.t[i]]))
            self.yanalytic[i+1] = yanalytic_eq(params_y) 
            if ( self.y[i+1] < min_position):
                stop_i = i+2
                break
        if stop_i != self.n:
            self.t = self.t[0:stop_i]
            self.a = self.a[0:stop_i]
            self.v = self.v[0:stop_i]
            self.y = self.y[0:stop_i]
            self.yanalytic = self.yanalytic[0:stop_i]
        params_a = np.concatenate((self.params_a, [self.v[-1], self.y[-1], self.t[-1]]))
        self.a[-1] = acceleration_eq (params_a) 
    ###############################################
    
    ###############################################
    # VELOCITY_VERLET METHOD
    def velocity_verlet (self, min_position, acceleration_eq, yanalytic_eq):
        stop_i = self.n
        # Start integrating using Euler's method
        for i in range(self.n-1):
            # expression for acceleration
            params_a = np.concatenate((self.params_a, [self.v[i], self.y[i], self.t[i]]))
            self.a[i] = acceleration_eq (params_a) 
            # update velocity and position
            self.y[i+1] = self.y[i] + self.DeltaT*self.v[i] + 0.5*(self.DeltaT**2)*self.a[i]
            params_a = np.concatenate((self.params_a, [self.v[i], self.y[i+1], self.t[i]]))
            self.a[i+1] = acceleration_eq (params_a)
            self.v[i+1] = self.v[i] + 0.5*self.DeltaT*(self.a[i]+self.a[i+1])
            # update time to next time step and compute analytical answer
            self.t[i+1] = self.t[i] + self.DeltaT
            params_y = np.concatenate((self.params_y, [self.v[i], self.y[i], self.t[i]]))
            self.yanalytic[i+1] = yanalytic_eq(params_y) 
            #if ( self.y[i+1] < min_position):
            #    stop_i = i+2
            #    break
        if stop_i != self.n:
            self.t = self.t[0:stop_i]
            self.a = self.a[0:stop_i]
            self.v = self.v[0:stop_i]
            self.y = self.y[0:stop_i]
            self.yanalytic = self.yanalytic[0:stop_i]
        params_a = np.concatenate((self.params_a, [self.v[-1], self.y[-1], self.t[-1]]))
        self.a[-1] = acceleration_eq (params_a) 
    ###############################################
    
    ###############################################
    # DISPSLAY THE DATA
    def display_data (self):
        data = {'t[s]': self.t,
                'y[m]': self.y-self.yanalytic,
                'v[m/s]': self.v,
                'a[m/s^2]': self.a
                }
        NewData = pd.DataFrame(data)
        display(NewData.head())
    ###############################################

    ###############################################
    # GRAPH THE DATA
    #finally we plot the data
    def graph_data (self):
        fig, axs = plt.subplots(3, 1)
        axs[0].plot(self.t, self.y, self.t, self.yanalytic)
        axs[0].set_ylabel('y and exact')
        axs[1].plot(self.t, self.v)
        axs[1].set_ylabel('v[m/s]')
        axs[2].plot(self.t, self.a)
        axs[2].set_xlabel('time[s]')
        axs[2].set_ylabel('a[m/s^2]')
        fig.tight_layout()
        plt.show()
    ###############################################
    
    ###############################################
    # GRAPH THE DATA
    def graph_data_2D (self):
        fig, axs = plt.subplots(3, 2)
        axs[0][0].plot(self.t, self.y[:,0], self.t, self.yanalytic[:,0])
        axs[0][0].set_ylabel('x and exact')
        axs[1][0].plot(self.t, self.v[:,0])
        axs[1][0].set_ylabel('vx[m/s]')
        axs[2][0].plot(self.t, self.a[:,0])
        axs[2][0].set_xlabel('time[s]')
        axs[2][0].set_ylabel('ax[m/s^2]')
        
        axs[0][1].plot(self.t, self.y[:,1], self.t, self.yanalytic[:,1])
        axs[0][1].set_ylabel('y and exact')
        axs[1][1].plot(self.t, self.v[:,1])
        axs[1][1].set_ylabel('vy[m/s]')
        axs[2][1].plot(self.t, self.a[:,1])
        axs[2][1].set_xlabel('time[s]')
        axs[2][1].set_ylabel('ay[m/s^2]')
        fig.tight_layout()
        plt.show()
    ###############################################


