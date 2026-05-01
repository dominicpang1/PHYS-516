import numpy as np
from numba import njit
lambd = -1.0
k = 1.0
T = 15.0
N = 1500
N_mc = 10**6
N_burn = 0
N_bar = 5 
delta = 0.2
xmax = 5.0

rng = np.random.default_rng()

@njit
def V(x):
    # real version, not imaginary 
    return -0.5 * lambd * x**2 + k * np.abs(x)**(2.0/3.0)

@njit
def total_action(path):
    dt = T / len(path)
    dx = np.diff(path)
    kinetic = 0.5 * dt**2 * np.sum(dx * dx)
    potential = np.sum(V(path))
    return dt * (kinetic + potential)

@njit
def delta_action(path, j, x_new, dt):
    x_old = path[j]
    dS = 0.0

    # bond (j-1, j)
    if j > 0:
        left = path[j - 1]
        dS += 0.5 * dt**3 * (((x_new - left)**2) - ((x_old - left)**2))

    # bond (j, j+1)
    if j < len(path) - 1:
        right = path[j + 1]
        dS += 0.5 * dt**3 * (((right - x_new)**2) - ((right - x_old)**2))

    # local potential
    dS += dt * (V(x_new) - V(x_old))
    return dS
@njit
def sweep(path, S,dt): # one monte carlo step
        for j in range(1, len(path)-1):   # keep path[0] fixed if that is your boundary,
                                        # the -1 makes other endpoint fixed
            x_new = path[j] + np.random.uniform(-delta, delta)
            dS = delta_action(path, j, x_new, dt)

            if dS <= 0.0 or np.random.random() < np.exp(-dS):
                path[j] = x_new
                S += dS
        return S
@njit
def mcmc(path, N_mc, N_burn,samples):
    path = path.copy()
    dt = T / len(path)

    S = total_action(path)
    
    for i in range(N_burn):
        S = sweep(path, S,dt)
    transitionamp = np.exp(-S)

    saveidx=0
    for i in range(N_mc):
        if i % 10000 == 0:
            print(f"Run {i} / {N_mc}")
        S = sweep(path, S,dt)
        if i % N_bar ==0:
            transitionamp = transitionamp +np.exp(-S)
            samples[saveidx,:]=path
        # determine when to add these amps - skip rows?
    #expectation = np.mean([energy_of_path(p) for p in sampled])
    return samples, transitionamp

def pathgrid(N,start,end):
    path = np.random.uniform(-xmax, xmax, size=N)
    path[0] = start
    if isinstance(end, (int, float)):
        path[-1] = end
    return path

@njit
def energy_of_path(path):
    dt = T / len(path)
    kinetic = 0.0
    potential = 0.0
    
    for i in range(len(path)-1):
        kinetic += 0.5 * ((path[i+1] - path[i]) / dt)**2
        potential += V(path[i])
    
    return (kinetic + potential) / len(path)

def main():
    wavefunc = []
    # A = np.linspace(-1.5,1.5,50)
    # for i in A:
    #     path = pathgrid(N,0,i)
    #     transitionamp = mcmc(path, N_mc, N_burn)
    #     wavefunc.append(transitionamp)
    #     with open("wavefunc.csv",'a') as file:
    #         file.write(str(transitionamp)+'\n')
    n_saved = N_mc // N_bar
    samples = np.empty((n_saved, N), dtype=np.float64)
    path = pathgrid(N,0,'rand')
    samples,transitionamp = mcmc(path, N_mc, N_burn, samples)
    midpoint = samples[:,N//2]



    import matplotlib.pyplot as plt
    print(wavefunc)
    fig, ax = plt.subplots()
    #ax.scatter(A,wavefunc)
    print(midpoint.min(), midpoint.max(), midpoint.mean(), midpoint.std())
    lo, hi = np.percentile(midpoint, [5, 95])
    plt.hist(midpoint, bins=400, range=(lo, hi), density=True)
   
    plt.show()

if __name__ == "__main__":
    main()