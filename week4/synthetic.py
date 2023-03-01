import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy import stats

def readFile():
  file = open("distr1.dat", "r")

  lines = [line[:-1] for line in file.readlines()]

  x = [int(line.split(" ")[0]) for line in lines]
  y = [int(line.split(" ")[1]) for line in lines]
  print("")

samples = np.random.poisson(3, size=100)

print(samples)
plt.hist(samples, bins=100)
plt.show()

# plt.plot(x, y)
# plt.scatter(counts)

# plt.show()
# readFile()