import numpy as np
import matplotlib.pyplot as plt

file = open("./sand_pile/statistics.dat", "r")

lines = [line[:-1] for line in file.readlines()]

# Remove titles
lines.pop(0)
# Get the ntopple with some magic
ntopple = []

for line in lines: 
  try:
    num = int(line.split()[1])
    ntopple.append(num)
  except:
    print("")
s = np.array(ntopple)

plt.hist(s, 10000, density=True)
# plt.scatter(s, s**(-0.0001), s=1)
plt.show()