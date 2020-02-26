from math import sin, pi
import numpy as np
from sympy import Symbol, integrate
import matplotlib.pyplot as plt
# function for the trapezoidal rule
def Trapez(a,b,f,n):
   h = (b-a)/float(n)
   s = 0
   x = a
   for i in range(1,n,1):
       x = x+h
       s = s+ f(x)
   s = 0.5*(f(a)+f(b)) +s
   return h*s
# function to integrate
def function(x):
    return sin(2*pi*x)
# define integration limits and integration points
a = 0.0; b = 0.5;
n = 100
Exact = 1./pi
print("Relative error= ", abs( (Trapez(a,b,function,n)-Exact)/Exact))
