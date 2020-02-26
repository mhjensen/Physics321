from math import sin, pi
import numpy as np
from sympy import Symbol, integrate
import matplotlib.pyplot as plt
# function for the Rectangular rule
def Rectangular(a,b,f,n):
   h = (b-a)/float(n)
   s = 0
   for i in range(0,n,1):
       x = (i+0.5)*h
       s = s+ f(x)
   return h*s
#  function to compute pi
def function(x):
    return sin(2*pi*x)
# define integration limits and integration points
a = 0.0; b = 0.5;
n = 100
Exact = 1./pi
print("Relative error= ", abs( (Rectangular(a,b,function,n)-Exact)/Exact))
