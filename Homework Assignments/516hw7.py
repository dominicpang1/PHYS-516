import numpy as np
import matplotlib.pyplot as plt
import random
import cmath
g = 1.0
M = 10.0
N=100
x = np.linspace(-M,M,N)
step = x[1]-x[0]

T = np.zeros((N,N))
for idx,row in enumerate(T):
    T[idx, idx] = 1 / (step * step)
    if idx!=0:
        T[idx, idx - 1] = -0.5 * (step ** -2)
    if idx!=len(row)-1:
        T[idx,idx+1] = -0.5 * (step ** -2)
print(T)
V = np.zeros_like(T)
for idx,row in enumerate(V):
    V[idx,idx]  = 0.5 * (x[idx]**2) + g * (x[idx]**4)
H = T+V
mu = 15000.0
H = mu*np.eye(N)-H #

v_0 = [2*random.random()-1 for i in range(N)]
eigenval = 0
previous = 0
diff = 1.0
count= 0
while diff > 0.00000001:
    w = np.zeros(N)
    # matrix multiplication w_k+1 = A v_k
    for i in range(N):
        w[i] = sum(H[i]*v_0)
    # v_k+1 = w_k+1/mag
    mag = np.sqrt(sum([w[j]*w[j] for j in range(N)]))
    v_0 = w/mag
    # matrix multiplication Av in lambda = v_+ Av
    Av = [sum(H[i]*v_0) for i in range(N)]
    # estimate eigenvalue
    eigenval = sum([v_0[j]*Av[j] for j in range(N)])
    diff = np.abs(eigenval - previous)
    previous = eigenval
    count = count + 1

print(count)
print("Discretized grid from -",M,"to",M, "with",N,"points.")
print("Ground state energy:",mu-eigenval)
print("Ground state wavefunction:",v_0)
plt.scatter(x,v_0,label = 'Wavefunction')
plt.show()
