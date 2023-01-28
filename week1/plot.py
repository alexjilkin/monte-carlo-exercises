import numpy as np
import matplotlib.pyplot as plt
import lcg

# Generates plot images for all types of RNGs, for 100 and 10000 points.
def generate_plot_images():
  lcg.seed_lcg(123)
  lcg_results = np.array([lcg.rand_lcg() for idx in range(100)])
  plt.plot(lcg_results, 'ro', markersize=1)

  plt.savefig('lcg 100p.png')
  plt.cla()

  lcg.seed_lcg(123)
  lcg_results = np.array([lcg.rand_lcg() for idx in range(10000)])
  plt.plot(lcg_results, 'ro', markersize=1)

  plt.savefig('lcg 10000p.png')
  plt.cla()

  lcg.seed_pm(123)
  pm_results = np.array([lcg.rand_pm() for idx in range(100)])
  plt.plot(pm_results, 'bs',  markersize=1)

  plt.savefig('pm 100p.png')
  plt.cla()

  lcg.seed_pm(123)
  pm_results = np.array([lcg.rand_pm() for idx in range(10000)])
  plt.plot(pm_results, 'bs',  markersize=1)
  plt.savefig('pm 10000p.png')
  plt.cla()

  lcg.seed_twister(123)
  pm_results = np.array([lcg.rand_twister() for idx in range(100)])
  plt.plot(pm_results, 'go', markersize=1)

  plt.savefig('twister 100p.png')
  plt.cla()

  lcg.seed_twister(123)
  pm_results = np.array([lcg.rand_twister() for idx in range(10000)])
  plt.plot(pm_results, 'go', markersize=1)

  plt.savefig('twister 10000p.png')
  plt.cla()


# Plots only at the range of < 0.02 or > 0.98
def plot_small_range():
  lcg.seed_lcg(1)
  pm_results = np.empty(1000)
  n = 0

  while (n < 1000):
    res = lcg.rand_lcg()
    
    if (res < 0.02 or res > 0.98):
      pm_results[n] = res
      n += 1

  plt.plot(pm_results, 'bs', markersize=1)
  plt.show()

plot_small_range()
# generate_plot_images()