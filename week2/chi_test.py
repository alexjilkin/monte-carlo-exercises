import numpy as np
import matplotlib.pyplot as plt
import qcg
import lcg

import math

qcg.seed_qcg(123124)
lcg.seed_lcg(1235)
lcg.seed_pm(12144)
lcg.seed_twister(4444)

# Get chi^2 value based on the RNG rand_fun = RNG function; M = number of bins
# Returns tuple (chi squared, array of bins count)
def get_chi(rand_func, M):
  N = 10 ** 5
  rand = rand_func
    
  bin_size = 1 / M

  bins = [[] for i in range(M)]

  # Create N random numbers and puts them in bins
  for i in range(0, N):
    num = rand()
    bin_index = math.floor(num / bin_size)

    bins[bin_index].append(num)

  # Size of bins
  y = np.array([len(a) for a in bins])
  E = N / M

  chi_arr = ((y - E)**2) / E
  chi = np.sum(chi_arr)
  return chi


def print_chi_average_median():
  chis_array = np.array([get_chi(lcg.rand_twister, 100) for i in range(0, 2000)])
  chi_average = np.average(chis_array)
  chi_median = np.median(chis_array)

  plt.hist(chis_array, bins = 100, density=True)
  plt.show()
  print("For lcg, the average: {} and the median is: {}".format(chi_average, chi_median))

def print_chi_distribution():
  chis_array = np.array([get_chi(lcg.rand_twister, 100) for i in range(0, 2000)])

  plt.hist(chis_array, bins = 100, density=True)
  plt.show()

##
def plot_bins():
  chi, y = get_chi(lcg.rand_twister, 100)

  plt.bar([i for i in range(1, 101)], y)
  plt.show()

print_chi_distribution()
