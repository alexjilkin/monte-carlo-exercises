import random
import math
import numpy as np
import matplotlib.pyplot as plt

l = 2
d = 10
N = 100
power = 7

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

            # If p_hit is 0, just use real pi to not skew results.
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
        


def is_needle_hit(d, l): 
    angle = random.random() * (math.pi / 2)
    x = random.random() * (d / 2)

    return x <= ((l * np.sin(angle)) / 2)

def is_needle_hit_lcg(d, l): 
    angle = random.random() * (math.pi / 2)
    x = random.random() * (d / 2)

    return x <= ((l * np.sin(angle)) / 2)


main(is_needle_hit_lcg)