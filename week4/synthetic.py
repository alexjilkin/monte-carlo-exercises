import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy import stats

# Reads the data from distr1.dat, returns x, y from it.
def read_dat():
  file = open("distr1.dat", "r")

  lines = [line[:-1] for line in file.readlines()]

  x = np.array([int(line.split(" ")[0]) for line in lines])
  y = np.array([int(line.split(" ")[1]) for line in lines])
  # plt.plot(x, y)
  # plt.show()
  print("The mean is:{}".format((x * y).sum() / y.sum()))
  return x, y
  print("")

# Reads the data once
x, y = read_dat()

# Gives N random numbers distributed according to the given data at distr1.dat
def first_exp_rand(N):
  samples = []
  # Generate 100 samples
  while len(samples) < 100:
    # Get x at the [-40, 1480] interval divided by 40
    rand_x = np.random.randint(-1, 37) 
    rand_y = np.random.uniform(0, 1600) 
    if (rand_y < y[rand_x]):
      samples.append(rand_x*40)
  return np.array(samples)

# Generate synthetic data according to the first experiment. 
# Calculate the means and the the cdf to find the needed range
def first_experiment():
  means = [first_exp_rand(100).mean() for _ in range(10000)]
    
  # plt.hist(means, bins=100, density=True)
  # plt.show()
  y, bin_edges = np.histogram(means, bins=1000)
  pdf = y / sum(y)
  cdf = np.cumsum(pdf)
  
  plt.plot(bin_edges[1:], cdf, label="CDF")
  plt.legend()
  plt.show()
  
# Generate synthetic data according to poisson distr. 
# Calculate the mean and the the cdf to find the needed range
def poisson_experiment():
  means = [np.random.poisson(3, size=100).mean() for _ in range(1000)]
  # plt.hist(means, bins=1000 , density=True)
  y, bin_edges = np.histogram(means, bins=1000)
  pdf = y / sum(y)
  cdf = np.cumsum(pdf)

  plt.plot(bin_edges[1:], cdf, label="CDF")
  plt.legend()
  plt.show()


first_experiment()
poisson_experiment()