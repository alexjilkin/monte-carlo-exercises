import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.constants import Boltzmann as Kb

# Constants 
KbT = 8.6173324e-5 * 300
E_the = (3/2) * KbT
twopi = 2 / np.sqrt(np.pi)
N = 500
delta_max_opt = 0.52

# Our probability density function
def n(E):
  return twopi * (np.sqrt(E) / np.power(KbT, 3/2)) * np.exp(-E/KbT)

# Generates N numbers using the markov chain method
def markov_chain(N, delta_max):
  x0 = 1
  x = x0

  rho = n(x0)
  
  samples = []

  for N in range(N):
    x0 = x
    u = np.random.uniform(-1, 1)
    
    x_p = x + (u * delta_max)
    rho_p = n(x_p)

    if (rho_p / rho >= 1):
      x = x_p
      rho = n(x_p)
    else:
      u = np.random.uniform(0, 1)
      if (rho_p / rho >= u):
        x = x_p
        rho = n(x_p)
      else:
        x = x0
    
    samples.append(x)
  return np.array(samples)

# Calculates rms for the Maxwell-Boltzmann energy distribution.
# Using N_runs with N_points each.
def rms(N_runs, delta_max, N_points=1000):
  E_i = np.array([markov_chain(N_points, delta_max).mean() for _ in range(N_runs)])

  return np.sqrt(np.sum((E_i - E_the)**2) / N)

# Calculates the mean and rms using an optimal delta max.
# Plots the distribution along side the intended function.
def mean_rms():
  samples = markov_chain(10000, delta_max_opt)
  mean = samples.mean()

  print("mean: {}, rms: {}, E_theory:".format(mean, rms(N, delta_max_opt), E_the))

  plt.hist(samples, bins=100, density=True)
  plt.plot(np.linspace(0, 1, 1000), n(np.linspace(0, 1, 1000)))
  plt.show()

# Plots rms according to different amount of N_points
def rms_plot():
  
  N_points = [10**2, 10**3, 10**4, 10**5, 10**6]

  plt.plot(N_points, [rms(N, delta_max_opt, N_points=N_p) for N_p in N_points])
  plt.xlabel('N_points')
  plt.ylabel('rms')
  plt.show()

# Plots rms arroding to delta_max to find the optimal value of it.
def delta_max_plot():
  delta_max_arr = np.linspace(0.01, 10, 10)
  plt.plot(delta_max_arr, [rms(N, delta_max) for delta_max in delta_max_arr])
  plt.xlabel('∆E max')
  plt.ylabel('rms')
  plt.show()

# mean_rms()
rms_plot()
# print(n(0.1))