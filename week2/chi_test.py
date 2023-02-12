import numpy as np
import matplotlib.pyplot as plt
import qcg
import lcg
import scipy.stats as st
import math

qcg.seed_qcg(123124)
lcg.seed_lcg(1235)
lcg.seed_pm(12144)
lcg.seed_twister(4444)

# Get chi^2 value based on the RNG rand_fun = RNG function; M = number of bins
# Returns tuple (chi squared, array of bins count)
def get_chi(rand_func, M):
  N = 10 ** 6
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

# Prints the chi mean, median and percentiles for the given rand_func with 600 M=100 chis. Then it plots a distribution of those.
def print_chi_mean_median_distribution(rand_func):
  chis_array = np.array([get_chi(rand_func, 100) for i in range(0, 600)])
  chi_mean = np.mean(chis_array)
  chi_median = np.median(chis_array)

  lower_conf_05 = np.percentile(chis_array, 5)
  lower_conf_10 = np.percentile(chis_array, 10)

  upper_conf_95 = np.percentile(chis_array, 95)
  upper_conf_90 = np.percentile(chis_array, 90)


  print("Mean: {}, Median: {}, \n alpha=0.05 lower confidence: {}, upper confidence: {}\n alpha=0.1, lower confidence: {}, upper confidence: {},"
  .format(chi_mean, chi_median, lower_conf_05, upper_conf_95, lower_conf_10, upper_conf_90))

  plt.hist(chis_array, bins = 40, density=True)
  plt.show()

# Plots the bins distribution of one chi^2 calculation
def plot_bins():
  # To make it work you must return (chi, y) from get_chi. as we need the bins array specifically.
  chi, y = get_chi(lcg.rand_pm, 100)

  plt.bar([i for i in range(1, 101)], y)
  plt.show()

print_chi_mean_median_distribution(qcg.rand_qcg)
# plot_bins()
