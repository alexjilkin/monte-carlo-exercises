import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.constants import Boltzmann as Kb

# Constants
KbT = 8.6173324e-5 * 300
E_the = (3/2) * KbT
twopi = 2 / np.sqrt(np.pi)
N = 500

def n(E, delta_max):
  return twopi * (np.sqrt(E) / np.power(KbT, 3/2)) * np.exp(-E/KbT)

def markov_chain(N, delta_max):
  x0 = 1
  x = x0

  rho = n(x0, delta_max)
  
  samples = []

  for N in range(N):
    x0 = x
    u = np.random.uniform(-1, 1)
    
    x_p = x + (u * delta_max)
    rho_p = n(x_p, delta_max)

    if (rho_p / rho >= 1):
      x = x_p
      rho = n(x_p, delta_max)
    else:
      u = np.random.uniform(0, 1)
      if (rho_p / rho >= u):
        x = x_p
        rho = n(x_p, delta_max)
      else:
        x = x0
    
    samples.append(x)
  return np.array(samples)

# Calculates rms for the Maxwell-Boltzmann energy distribution.
def rms(N, delta_max):
  E_i = np.array([markov_chain(1000, delta_max).mean() for _ in range(N)])

  return np.sqrt(np.sum((E_i - E_the)**2) / N)

# Calculates the mean and rms using an optimal delta max.
# Plots the distribution along side the intended function.
def mean_rms():
  delta_max_opt = 0.52

  samples = markov_chain(10000, delta_max_opt)
  mean = samples.mean()

  print("mean: {}, rms: {}, E_theory:".format(mean, rms(N, delta_max_opt), E_the))

  plt.hist(samples, bins=100, density=True)
  plt.plot(np.linspace(0, 1, 1000), n(np.linspace(0, 1, 1000), delta_max_opt))
  plt.show()

def delta_max_plot():
  delta_max_arr = np.linspace(0.01, 10, 20)
  plt.plot(delta_max_arr, [rms(N, delta_max) for delta_max in delta_max_arr])
  plt.xlabel('∆E max')
  plt.ylabel('rms')
  plt.show()

mean_rms()
# delta_max_plot()
# print(n(0.1))