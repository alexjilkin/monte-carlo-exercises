import numpy as np
import random

seed = 0 # x_0
m = 1067089
# 1033 * 1033

def seed_qcg(s): 
  global seed
  seed = s

def rand_qcg():
  global seed
  global m

  a = 309900  #1033 * 4 * 5 * 15
  b = 3100 # b = 1 mod p_i
  c = 463

  x_n = ((a * seed * seed) + (b * seed) + c) % m
  seed = x_n

  return seed / m


def find_repeat():
  repeat_count = 0
  repeat_array = np.empty(m)
  n = 0

  while (repeat_count < 10):
    x_n = int(rand_qcg() * m)

    repeat_count = repeat_count + 1 if repeat_array[x_n] else 0
    repeat_array[x_n] = True
    
    n = n + 1

  return n - 10

seed_qcg(12312)

# print(find_repeat())

