import numpy as np
import time

N = 15
grid = np.zeros((N + 3, N + 3))
# grid = np.random.randint(2, size=(N + 3, N + 3))

grid[5, 5] = 1
grid[5,6] = 1
grid[6,5] = 1
grid[6,6] = 1

grid[7, 7] = 1
grid[7,8] = 1
grid[8,7] = 1
grid[8,8] = 1


grid[2,2] = 1
grid[2,3] = 1
grid[2,4] = 1

grid[9,1] = 1
grid[9,2] = 1
grid[8,3] = 1

grid[7,2] = 1
grid[7,3] = 1
grid[7,4] = 1
grid[5,2] = 1

def sum_neighbords(i, j):
  return grid[i + 1][j] + grid[i][j + 1] + grid[i - 1][j] + grid[i][j - 1] + grid[i + 1][j + 1] + grid[i - 1][j - 1] + grid[i + 1][j - 1] + grid[i - 1][j + 1]

while True:
  for i in range(1, N ):
    for j in range(1, N):
      print ("x" if grid[i][j] == 1 else " ", end=" ")
    print("\n")
  print("-------------------------------- \n \n")
  time.sleep(0.5)

  next_grid = grid.copy()

  for i in range(1, N):
    for j in range(1, N):
      sum = sum_neighbords(i, j)
      if (grid[i][j] == 0):
        if(sum == 3):
          next_grid[i][j] = 1
      else:
        if (sum < 2):
           next_grid[i][j] = 0
        elif (sum == 2 or sum == 3):
           next_grid[i][j] = 1
        elif (sum > 3):
           next_grid[i][j] = 0
  grid = next_grid.copy()
  

      

