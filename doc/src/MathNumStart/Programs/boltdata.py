import numpy as np
import matplotlib.pyplot as plt
# we just initialize time and position
x = np.array([10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0])
t = np.array([1.85, 2.87, 3.78, 4.65, 5.50, 6.32, 7.14, 7.96, 8.79, 9.69])
plt.plot(t,x, color='black')
plt.xlabel("Time t[s]")
plt.ylabel("Position x[m]")
plt.title("Usain Bolt's world record run")
plt.show()
