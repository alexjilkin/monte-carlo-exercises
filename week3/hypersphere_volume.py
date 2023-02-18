import random 
import numpy as np

r = 1

def volume(N):
  dots = []
  hit_dots = []

  for k in range(0, 1000):
    dot = np.array([random.uniform(-r, r) for i in range(0, N)])
    dots.append(dot)

    sq = np.sum(dot**2)
    if sq < r**2:
      hit_dots.append(dot)

  volume = ((2*r)**N) * (len(hit_dots) / len(dots))

  return volume

sample_size = 100

for dim in range(1, 16):
  volumes = [volume(dim) for i in range(0, sample_size)]

  mean = np.mean(volumes)
  std_deviation = np.std(volumes)

  print("{}-sphere: mean volume: {} and std-deviation: {}".format(dim, mean, std_deviation))

