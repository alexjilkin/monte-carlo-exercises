import random
import math
import numpy as np
import matplotlib.pyplot as plt
import lcg

l = 2
d = 10
N = 10
power = 7
lcg.seed_lcg(12355)

# times = [10, 100, 1000...., 10^7]
tens_power_arr = np.power(np.full(power, 10, dtype=int), np.arange(1, power + 1))

# Gets is_hit_func(d, l) to accomodate question 4 that asks to use different RNG
def main(is_hit_func):
    error_data = np.array([])

    for n in tens_power_arr:
        error_sum = 0

        # Run same experiment N times
        for _ in range(0, N):  
            hit_count = 0

            # Throw needle n times
            for _ in range(0, n):
                hit_count += 1 if is_hit_func(d, l) else 0

            p_hit = hit_count / n

            # Calculates pi using buffon's "formula", with safety for  p_hit == 0
            pi = 2 * l / (p_hit * d) if p_hit != 0 else np.pi
            error_sum += np.abs((np.pi - pi))
            print("n: {}, pi: {}".format(n, pi))
        
        average_error = error_sum / N
        error_data = np.append(error_data, average_error)
    print(error_data)
  
    x = tens_power_arr;
    y = error_data

    plt.xlabel("Needle throw times")
    plt.ylabel("Average pi error")
    plt.xscale('log')
    plt.scatter(x, y)
    plt.show()
        

# Checks hit using python's random if needle hit
def is_needle_hit(d, l): 
    angle = random.random() * (math.pi / 2)
    x = random.random() * (d / 2)

    return x <= ((l * np.sin(angle)) / 2)

# Checks hit using basic LCG method random from lcg.py file if needle hit
def is_needle_hit_lcg(d, l): 
    angle = lcg.rand_lcg() * (math.pi / 2)
    x = lcg.rand_lcg() * (d / 2)

    return x <= ((l * np.sin(angle)) / 2)


main(is_needle_hit)