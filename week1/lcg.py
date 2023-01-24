import numpy as np

lcg_seed = 0 # x_0
pm_seed = 0 # x_0

def seed_lcg(seed): 
  global lcg_seed
  lcg_seed = seed

def seed_pm(seed): 
  global pm_seed
  pm_seed = seed

def rand_lcg():
  global lcg_seed
  a = 587
  c = 1019
  m = 113829760

  lcg_seed = ((a * lcg_seed) + c) % m
  return ((a * lcg_seed) + c) % m

def rand_pm():
  global pm_seed
  m = 2147483647
  q = 127773
  r = 2836 

  a = 16807

  k = pm_seed / q
  x_n = a * (pm_seed - (k * q)) - (r * k)

  if x_n < 0:
    x_n = x_n + m
  pm_seed = x_n * a
  return x_n



def find_repeat():
  seed_lcg(112312312)
  repeat_count = 0
  repeat_array = np.empty(113829760, dtype=float)
  n = 0

  while (repeat_count < 3):
    x_n = int(rand_lcg())
    
    repeat_count = repeat_count + 1 if repeat_array[x_n] == True else 0

    repeat_array[x_n] = True
    n = n + 1

  print(n)


find_repeat()

# seed_pm(2)

# print(rand_pm())
# print(rand_pm())
# print(rand_pm())
# print(rand_pm())
# print(rand_pm())
# print(rand_pm())