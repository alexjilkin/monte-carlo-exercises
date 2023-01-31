import numpy as np
import matplotlib.pyplot as plt
import qcg
import lcg

import math

qcg.seed_qcg(123124)
lcg.seed_lcg(1235)
lcg.seed_pm(12144)
lcg.seed_twister(4444)

def get_chi():
  N = 1000000
  M = 100
  
  bin_size = 1 / M

  bins = [[] for i in range(M)]

  # Create N random numbers and puts them in bins
  for i in range(0, N):
    num = lcg.rand_twister()
    bin_index = math.floor(num / bin_size)

    bins[bin_index].append(num)

  # Size of bins
  y = np.array([len(a) for a in bins])
  E = N / M

  chi_arr = ((y - E)**2) / E
  chi = np.sum(chi_arr)
  print(chi)

get_chi()
get_chi()
get_chi()
get_chi()

