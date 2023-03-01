import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.constants import Boltzmann as Kb

KbT = 8.6173324e-5 * 300

twopi = 2 / np.sqrt(np.pi)

def n(E):
  return twopi * (np.sqrt(E) / np.power(KbT, 3/2)) * np.exp(-E/KbT)

def markov_chain(N):
  x0 = 1
  x = x0

  rho = n(x0)
  delta_max = 0.5
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
  return samples

samples = markov_chain(10000)
plt.hist(samples, bins=100, density=True)
plt.plot(np.linspace(0, 1, 1000), n(np.linspace(0, 1, 1000)))
plt.show()
# print(n(0.1))