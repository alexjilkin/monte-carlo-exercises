import numpy as np
import matplotlib.pyplot as plt
import random 

def f(x):
  return 4 / (x**2 + 4)

def F_inverse(u):
  return 2*np.tan(u / 2)

nums = [F_inverse(random.random()) for i in range(0, 10000)]

print(nums)
# plt.hist(nums, bins = 100, density=True)
# plt.show()


# Plots the given function as argument
def plot(f):
  x = np.linspace(-10, 10, 10000)
  plt.plot(x, f(x))
  
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.grid()
  plt.show()

plot(f)

