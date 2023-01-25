import numpy as np
import matplotlib.pyplot as plt
import lcg

lcg.seed_lcg(123)

lcg_results = np.array([lcg.rand_lcg() for idx in range(100)])
lcg.seed_pm(123)

pm_results = np.array([lcg.rand_pm() for idx in range(100)])

plt.plot(lcg_results, 'ro', pm_results, 'bs')

plt.show() 