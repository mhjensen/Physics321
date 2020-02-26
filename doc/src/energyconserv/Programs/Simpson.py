from math import sin, pi
import numpy as np
from sympy import Symbol, integrate
# function for the trapezoidal rule
def Simpson(a,b,f,n):
   h = (b-a)/float(n)
   sum = f(a)/float(2);
   for i in range(1,n):
       sum = sum + f(a+i*h)*(3+(-1)**(i+1))
   sum = sum + f(b)/float(2)
   return sum*h/3.0
# function to integrate
def function(x):
    return sin(2*pi*x)
# define integration limits and integration points
a = 0.0; b = 0.5;
n = 100
Exact = 1./pi
print("Relative error= ", abs( (Simpson(a,b,function,n)-Exact)/Exact))
