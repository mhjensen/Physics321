# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
import os

def freefall_acceleration (g, D, v):
    return -g + D*v*v

def freefall_yanalytic (g, D, y_0, t, v_0=0):
    vT = sqrt(g/D)
    return y_0-(vT*vT/g)*log(cosh(g*t/vT))

def freefall_no_drag_acceleration  (g, D, v): #Arguments must be in the same order
    return -g

def freefall_no_drag_yanalytic (g, D, y_0, t, v_0):
    return -0.5*g*t**2 + v_0*t + y_0    

class ClassicalMechanicsSolvers ():
    def __init__(self, g, D, DeltaT, tfinal, v_0, y_0):
        self.g = g
        self.D = D
        self.set_up_time (DeltaT, tfinal)
        self.set_up_initial_arrays (v_0, y_0)
        
    ###############################################
    # SETTING UP TIME
    def set_up_time (self, DeltaT, tfinal):
        self.DeltaT = DeltaT
        self.n = ceil(tfinal/DeltaT)
        self.t = np.zeros(self.n)
    ###############################################

    ###############################################
    # SETTING UP THE INITIAL ARRAYS
    def set_up_initial_arrays (self, v_0, y_0): ## No longer need n as an argument
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
    # EULER'S METHOD
    def euler (self, min_position, acceleration_eq, yanalytic_eq):
        i_stop = self.n
        # Start integrating using Euler's method
        for i in range(self.n-1):
            # expression for acceleration
            self.a[i] = acceleration_eq (self.g, self.D, self.v[i]) 
            # update velocity and position
            self.y[i+1] = self.y[i] + self.DeltaT*self.v[i]
            self.v[i+1] = self.v[i] + self.DeltaT*self.a[i]
            # update time to next time step and compute analytical answer
            self.t[i+1] = self.t[i] + self.DeltaT
            self.yanalytic[i+1] = yanalytic_eq(self.g, self.D, self.y[0], self.t[i+1], self.v[0]) 
            if ( self.y[i+1] < min_position):
                stop_i = i+2
                break
        if stop_i != self.n:
            self.t = self.t[0:stop_i]
            self.a = self.a[0:stop_i]
            self.v = self.v[0:stop_i]
            self.y = self.y[0:stop_i]
            self.yanalytic = self.yanalytic[0:stop_i]
        self.a[-1] = acceleration_eq (self.g, self.D, self.v[-1]) 
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