import numpy as np
import random
#parameters
M = 10
N = 1000

def energy(grid,J=1,h=1):
    sum1 = 0
    sum2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            sum2 = sum2 + grid[i][j]
            sum1 = sum1 + grid[i][j]*(grid[i][j-1]+grid[i-1,j])
            # above avoids double counting by counting the interacting with the item behind and above
    return J*sum1 + h*sum2

def makegrid(L):
    grid = np.zeros([L,L])
    for i in range(L):
        for j in range(L):
            grid[i][j] = random.choice([-1,1])
    return grid

def main():
    grid = makegrid(4)
    print(grid)
    print(energy(grid))

if __name__ == '__main__':
    main()
