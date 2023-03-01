import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy import stats

def poisson(x, lam):
  return ((np.power(lam, x)) * np.exp(-lam)) / gamma(x + 1)

file = open("distr1.dat", "r")

lines = [line[:-1] for line in file.readlines()]

x = [int(line.split(" ")[0]) for line in lines]
y = [int(line.split(" ")[1]) for line in lines]

s = np.random.poisson(3, size=10000)

# plt.plot(x, y)
plt.hist(s, bins = 14, density=True)

plt.show()
