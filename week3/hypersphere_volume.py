import random 
import numpy as np

r = 1

def volume(N):
  dots = []
  hit_dots = []

  for k in range(0, 10000):
    dot = np.array([random.uniform(-r, r) for i in range(0, N)])
    dots.append(dot)

    sq = np.sum(dot**2)
    if sq < r**2:
      hit_dots.append(dot)

  volume = ((2*r)**N) * (len(hit_dots) / len(dots))

  return volume

N = 3
sample_size = 100

volumes = [volume(3) for i in range(0, sample_size)]
mean = np.mean(volumes)
std_deviation = np.std(volumes)

print("For a {}-sphere we get a mean volume: {} and std-deviation: {}".format(N, mean, std_deviation))
