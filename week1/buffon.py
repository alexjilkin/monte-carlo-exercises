import random
import math
import numpy as np

l = 2
d = 10
N = 2

def main():
  error_data = np.array([])

  # n = 10, 100 .... 10^7
  for i in range(1, 7):
      n = np.power(10, i)
      error_sum = 0

      # Run same experiment N times
      for _ in range(0, N):  
        hit_count = 0

        # Throw needle n times
        for _ in range(0, n):
          hit_count += 1 if isNeedleHit(d, l) else 0

        p_hit = hit_count / n
        pi = 2 * l / (p_hit * d)
        error_sum += np.abs((np.pi - pi))
        print("n: {}, pi: {}".format(n, pi))
      
      average_error = error_sum / N
      error_data = np.append(error_data, average_error)
  print(error_data)    
        


def isNeedleHit(d, l): 
  angle = random.random() * (math.pi / 2)
  x = random.random() * (d / 2)

  return x <= ((l * np.sin(angle)) / 2)

main()