import random 
import numpy as np
from scipy.special import gamma
from scipy import stats
import matplotlib.pyplot as plt
import time
import vdc

a = 0
b = 20

def poisson(x, lam):
  return ((np.power(lam, x)) * np.exp(-lam)) / gamma(x + 1)

def f(x):
  return poisson(x, 2)
def g(x):
  return poisson(x, 0.5)


# Integrates f(x) using direct sampling, and the given RNG rand
def direct_sampling(N, rand = random.uniform):
  samples = np.array([f(rand(a, b)) for _ in range(0, N)])

  return ((b - a) / N) * samples.sum()
   
# Returns an array of N partially stratifed in 100 bins random numbers between a and b
def partially_stratified_sampling(N, rand = random.uniform):
  grids = 32
  samples = []
  size = (b - a) / grids

  for i in range(0, grids):
      samples.append([f(rand(i * size, (i + 1) * size)) for _ in range(0, int(N / grids))])

  return ((b - a) / N) * np.array(samples).sum()

# Return an array of stratified random number between b and a
def stratified_sampling(N, rand = random.uniform):
  size = (b - a) / N

  samples = [f(rand(i * size, (i + 1) * size)) for i in range(0, int(N))]

  return ((b - a) / N) * np.array(samples).sum()

# Calculated max between 10 ** 6 samples to get 0.28798114136535946
def hit_miss(N, rand = random.uniform):
  max = 0.29
  v = max * (b - a)
  samples = []

  for _ in range(0, N):
    x = rand(a, b)
    y = rand(0, max)

    samples.extend([y] if y <= f(x) else [])

  return v * (len(samples) / N)

# Calculates the integral of f using importance sampling
def importance_sampling(N):
  # RNG for poisson distribution function. I use it directly instead of calculating the inverse my self.
  r = np.array([stats.poisson.rvs(mu = 0.5) for _ in range(0, N)])

  return np.sum(f(r) / g(r)) * (1 / N)

samples = [10**2, 10**3, 10**4, 10**5, 10**6]
methods = [direct_sampling, hit_miss, partially_stratified_sampling, stratified_sampling, importance_sampling]

I_exact = 0.947019421085

# Runs all methods and prints results
def evaluate():
  for N in samples:

    for method in methods:
      st = time.time()
      res = method(N)
      et = time.time()

      # printing while limiting the float number for better readability
      print("N={}, {}:  I={:.11f} in {:.5f}s Δ𝐼={}".format(N, method.__name__, res, et - st, I_exact - res))

# Runs all methods and evaluates the mean standard error of them.
def evaluate_error():
  N = 10**4

  for method in methods:
    res = [method(N) for _ in range(100)]
    print("{} standard error: {}".format(method.__name__, np.std(res)))

def evaluate_van_der():
  # Multiplied VDC number by 20 to cover the entire interval [0, 20]
  sequences_13 = [np.array([vdc.vdc(i, 17) * 20 for i in range(N)]) for N in samples]
  

evaluate()
#evaluate_error()
# evaluate_van_der()