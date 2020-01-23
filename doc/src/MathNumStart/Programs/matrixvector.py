
import numpy as np
#We define a  3 dimensional vector with random numbers
n = 3
a = np.random.rand(n)
# define a matrix of dimension 3 x 3 and set all elements to random numbers with x \in [0, 1]
R = np.random.rand(n, n)
print(a)
print(R)
b = R @ a.T
print(b)
