import numpy as np
import matplotlib.pyplot as plt
import random 
import math

def f(x):
  return 4 / (x**2 + 4)

def F_inverse(u):
  return 2*np.tan((np.pi * u) - (np.pi / 2))

nums = [F_inverse(random.random()) for i in range(0, 10000)]

# plt.hist(nums, bins = 1000)
# # plt.ylim(-5, 5)
# plt.show()


# Plots the given function as argument
def plot(f):
  x = np.linspace(-np.pi, np.pi, 1000)
  plt.plot(x, f(x))
  
  plt.ylim(-5, 5)
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

plot(F_inverse)

