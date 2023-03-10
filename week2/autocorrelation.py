import numpy as np
import matplotlib.pyplot as plt
import lcg
import lcg_shuffle

lcg.seed_lcg(1235)
lcg.seed_pm(12144)

# Calculates the auto correlation of rand_func
def get_autocorrelation(rand_func):
  N = 10 ** 5

  C = []
  x = np.array([(rand_func()) for x in range(0, N)])

  x_i = np.sum([x[i] for i in range(0, N) ]) / N
  x_i_sq = np.sum([(x[i] ** 2) for i in range(0, N) ]) / N

  for k in range(0, N):
    x_ik = 0

    x_ik = np.sum([x[i + k] * x[i] for i in range(0, N - 1 - k) ]) / (N - k)

    C.append((x_ik - x_i**2) / (x_i_sq - x_i**2))
    if (k % 1000 == 0):
      print(k)

  return C


# The autocorrelations of the shuffle lcg.
correlations = get_autocorrelation(lcg_shuffle.rand_lcg_shuffle)

plt.plot(correlations)
plt.show()
