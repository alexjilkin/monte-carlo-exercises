import numpy as np
import random


## ------------- Basic lcg -----------------------

lcg_seed = 0 # x_0
m_lcg = 113829760

def seed_lcg(seed): 
  global lcg_seed
  lcg_seed = seed

def rand_lcg():
  global lcg_seed
  a = 587
  c = 1019
  m = m_lcg

  x_n = ((a * lcg_seed) + c) % m
  lcg_seed = x_n

  return lcg_seed / m


## ------------- Park Miller -----------------------

pm_seed = 0 # x_0
m_pm = 2147483647

def seed_pm(seed): 
  global pm_seed
  pm_seed = seed

def rand_pm():
  global pm_seed
  x_n = pm_seed
  m = m_pm

  q = 127773
  r = 2836 
  a = 16807

  k = x_n // q
  x_n = a * (x_n - k * q) - r * k

  if (x_n < 0):
    x_n += m

  pm_seed = x_n

  return x_n / m

## ----------------- Twister using Python's random -----------------------------

twister_seed = 1

def seed_twister(seed):
    random.seed(seed)
def rand_twister():
    return random.random()


# dynamically uses different types of rng: type = lcg | pm | twister
# saves all results in a dictionary and checks if the current giver random number 
# was given before.
def find_repeat(type):
  seed = globals()["seed_{}".format(type)]
  rand = globals()["rand_{}".format(type)]

  seed(123)

  repeat_count = 0
  repeat_dictionary = {}
  n = 0

  while (repeat_count < 10):
    x_n = rand() 

    repeat_count = repeat_count + 1 if x_n in repeat_dictionary else 0
    repeat_dictionary[x_n] = True
    if (n % 10000000 == 0):
      print(n)
    n = n + 1

  print(n)


# print(rand_twister())
# print(rand_lcg())
# print(rand_lcg())
# print(rand_lcg())

# find_repeat("pm")