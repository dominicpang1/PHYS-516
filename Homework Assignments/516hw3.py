# Metropolis Hastings for 2D Ising Model
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

def mcmc(N,M,L,J=1,h=1,B=1):
    grid = np.zeros([L,L])
    for i in range(L):
        for j in range(L):
            grid[i][j] = random.choice([-1,1])
    average_energies = []
    average_energies_squared =[]
    for i in range(M):
        energies = []
        energies_squared =[]
        for j in range(N):
            candidate_grid = grid.copy()
            x = random.randint(0,L-1)
            y = random.randint(0,L-1)
            candidate_grid[x][y]=candidate_grid[x][y]*-1
            e_prime = energy(candidate_grid,J,h)
            e = energy(grid,J,h)

            energies_squared.append(e**2)
            energies.append(e) 
            ratio = np.exp(-B*(e_prime-e))
            if ratio < 1:
                if random.random()>ratio:
                    grid = candidate_grid
            if ratio > 1:
                grid = candidate_grid
        average_energies.append(np.mean(energies))
        average_energies_squared.append(np.mean(energies_squared))
    return np.mean(average_energies),np.std(average_energies)/np.sqrt(M), np.mean(average_energies_squared),np.std(average_energies_squared)/np.sqrt(M)


def main():
    E,err_E,E_2, err_E_2 = mcmc(10000,100,10,1,1,1)
    print("energy:",E,"with std",err_E)
    print("energy squared:", E_2, "with std", err_E_2)
if __name__ == '__main__':
    main()