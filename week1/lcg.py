import numpy as np
import random

## ------------- Basic lcg -----------------------

lcg_seed = 0 # x_0
m_lcg = 113829760
# 2 x 2 x 2 x 2 x 2 x 2 x 2 x 5 x 11 x 19 x 23 x 37

def seed_lcg(seed): 
  global lcg_seed
  lcg_seed = seed

def rand_lcg():
  global lcg_seed
  a = 3557181
  c = 5561
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

m_twister = 2147483647 # Just to be used at the find_repeat function
twister_seed = 1

def seed_twister(seed):
    random.seed(seed)
def rand_twister():
    return random.random()


# dynamically uses different types of rng: type = lcg | pm | twister
# saves all results in a dictionary/array and checks if the current giver random number 
# was given before.
def find_repeat(type):
  seed = globals()["seed_{}".format(type)]
  rand = globals()["rand_{}".format(type)]
  m = globals()["m_{}".format(type)]
  seed(123)

  repeat_count = 0
  repeat_array = np.empty(m)
  n = 0

  while (repeat_count < 10):
    x_n = int(rand() * m)

    repeat_count = repeat_count + 1 if repeat_array[x_n] else 0
    repeat_array[x_n] = True
    
    n = n + 1

  print(n)
  return n

# Just a main, I think maybe the exercise required it.
def main():
  seed_lcg(98444);   
  a=rand_lcg();  
  seed_pm(7845);   
  b=rand_pm();  
  seed_twister(4341); 
  c=rand_twister();  
  print("LCG value: {}; Park-Miller value: {}; Mersenne twister: {} \n".format(a, b, c));
  lcg_repeat_count = find_repeat("lcg")

  print("LCG with a=3557181 c=5561 period:{}".format(lcg_repeat_count));


main()