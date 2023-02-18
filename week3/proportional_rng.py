import numpy as np
import matplotlib.pyplot as plt
import random 
import math

def f(x):
  return 4 / (x**2 + 4)

# Normalized by F(infinity) = pi
def F_inverse(u):
  return (2 * np.tan(np.pi * (u - 1/2))) / np.pi

def rand_proportional():
  u = random.random()
  x = F_inverse(u)

  while (x < -10) | (x > 10):
    u = random.random()
    x = F_inverse(u)
  
  return x

# Gets 10**5 random numbers proportional to f
def inversion():
  x = np.array([rand_proportional() for i in range(0, 1000000)])

  plt.hist(x, bins = 1000, density=True)
  plt.plot(np.linspace(-10, 10, 1000), f(np.linspace(-10, 10, 1000)))
  plt.show()

# Gets a random tuple (x, y) with a Gaussian distribution using Box-Muller method
def box_muller_rand():
  u1 = random.random()
  psi = 2 * np.pi * u1

  u2 = random.random()
  r = np.sqrt(-2 * np.log(u2))

  return r * np.cos(psi), r * np.sin(psi)

# Gets 10**5 random numbers using combined hit&miss and proportional
# to a Gaussian distribution function.
def combined():
  samples = []
  miss_count = 0

  while (len(samples) < 100000):
    x, y  = box_muller_rand()
    y = random.uniform(0, 2 * y)

    if (y > f(x)):
      miss_count += 1
    else:
      samples.append(x)

  plt.hist(samples, bins = 100, density=True)
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

combined()