import lcg
import random

size = 32
arr = [lcg.rand_lcg() for i in range(0, 32)]

# Shuffles an array of 32 with random numbers from an lcg RNG
def rand_lcg_shuffle():
  index = int(random.random() * size)
  num = arr[index]
  arr[index] = lcg.rand_lcg()

  return num