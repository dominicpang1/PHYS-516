import numpy as np
import matplotlib.pyplot as plt
import random 
# closed universe k = 1
# lambda determines what dark energy is  

# is each path a state
# get change in energy per new path rather than calculating and comparing actions
lambd = -1
k = 1 
T = 15
N=1500
N_mc = 10**6
N_burn = 0
delta = 0.2
n_bar = 5
x = 5

def mcmc(path,N_mc,N_burn,delta):
    path_final = path[:]
    for i in range(N_burn):
        S_old = action(path_final)
        # save time with action comparison
        for j in range(len(path)):
           randval = random.uniform(path_final[j]-delta,path_final[j]+delta)
           new_path = path_final[:]
           new_path[j]=randval
           S_new = action(new_path)
           if S_new < S_old:
               path_final = new_path
               S_old = S_new
           else:
               condition = random.random()
               if condition <= np.exp(S_old-S_new):
                   path_final = new_path
                   S_old = S_new
    for i in range(N_mc):
        print("Run",i,"out of 1000000")
        S_old = action(path_final)
        for j in range(len(path)):
           randval = random.uniform(path_final[j]-delta,path_final[j]+delta)
           new_path = path_final[:]
           new_path[j]=randval 
           S_new = action(new_path)
           if S_new < S_old:
               path_final = new_path
               S_old = S_new
           else:
               condition = random.random()
               if condition <= np.exp(S_old-S_new):
                   path_final = new_path
                   S_old = S_new
        
    return path_final

def action(path):
    lattice_spacing = T/len(path)
    act = 0
    for i in range(len(path)-1): 
        act = act + 0.5*(lattice_spacing**2)*(path[i+1]-path[i])**2- 0.5*lambd*path[i]**2+k*path[i]**(2/3)
    return lattice_spacing*act

def pathgrid(N):
    path = np.array([random.uniform(-x,x) for i in range(N)])
    path[0]=0 # HH condition
    return path
    
def main():
    path = pathgrid(N)
    
    final_path = mcmc(path,N_mc,N_burn,delta)
    x = np.linspace(0,len(path),N)
    # is A(t) linearly subdivided?
    fig,ax = plt.subplots()
    ax.plot(x,final_path,label = '')
    ax.plot(x,path )
    fig.show()

if __name__ == '__main__':
    main()