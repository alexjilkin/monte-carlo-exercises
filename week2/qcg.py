import numpy as np
import random

seed = 0 # x_0
m = 113829760

what are the prime factors of 113829760?
2, 3, 5, 7, 13, 17, 19, 31, 41, 43, 47, 61, 73, 83, 89, 97

def seed_lcg(s): 
  global seed
  seed = s

def rand_lcg():
  global lcg_seed
  a = 587
  c = 1019
  m = m_lcg

  x_n = ((a * lcg_seed) + c) % m
  lcg_seed = x_n

  return lcg_seed / m
