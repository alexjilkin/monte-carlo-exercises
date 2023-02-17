import numpy as np
import matplotlib.pyplot as plt
import random 
import math

def f(x):
  return 4 / (x**2 + 4)

def F_inverse(u):
  return 2 * np.tan(np.pi * (u - 1/2))

u = np.array([random.random() for i in range(0, 100000)])
x = F_inverse(u)
x = x[(x >= -10) & (x <= 10)]

plt.hist(x, bins = 100, density=True)
plt.plot(np.linspace(-10, 10, 1000), f(np.linspace(-10, 10, 1000)))
plt.show()


# Plots the given function as argument
def plot(f):
  x = np.linspace(-np.pi, np.pi, 1000)
  plt.plot(x, f(x))
  
  plt.ylim(-5, 5)
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

# plot(F_inverse)

