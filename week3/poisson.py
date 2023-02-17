import random 
import numpy as np
from scipy.special import gamma, factorial

N = 10 ** 5
a = 0
b = 20

def f(x):
  return ((np.power(2, x)) * np.exp(-2)) / gamma(x + 1)

def direct_sampling(N):
  samples = np.array([f(random.uniform(a, b)) for _ in range(0, N)])

  return ((b - a) / N) * samples.sum()
   
# Returns an array of N stratifed random numbers between a and b
def stratified_sampling(N, a, b):
  grids = 32
  samples = []
  size = (b - a) / grids

  for i in range(0, grids):
      samples.append([f(random.uniform(i * size, (i + 1) * size)) for _ in range(0, int(N / grids))])

  return ((b - a) / N) * np.array(samples).sum()

# Calculated max between 10 ** 6 samples to get 0.28798114136535946
def hit_miss(N):
  max = 0.29
  v = max * (b - a)
  samples = []

  for _ in range(0, N):
    x = random.uniform(a, b)
    y = random.uniform(0, max)

    samples.extend([y] if y <= f(x) else [])

  return v * (len(samples) / N)

# print(direct_sampling(N))
# print(hit_miss(N))
print(stratified_sampling(N, a, b))