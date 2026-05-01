import numpy as np
from numba import njit
import matplotlib.pyplot as plt
lambd = -1.0
k = 1

T = 15.0
N = 1500


@njit
def pathgrid(start,end,t,T,a,b,c):
    path = np.linspace(start,end,len(t))
    path = path + fourier_correction(t,T,a,b,c)
    return path

@njit
def fourier_correction(t,T,a,b,c):
    f1 = a*np.sin(1*np.pi*t/T)
    f2 = b*np.sin(2*np.pi*t/T)
    f3 = c*np.sin(3*np.pi*t/T)
    return f1 + f2 + f3 

@njit
def V(x,lambd,k):
    # real version, not imaginary 
    return -0.5 * lambd * x**2 + k * np.abs(x)**(2.0/3.0)

@njit
def total_action(path,T,lambd,k):
    dt = T / len(path)
    dx = np.diff(path)
    kinetic = 0.5 * dt**2 * np.sum(dx * dx)
    potential = np.sum(V(path,lambd,k))
    return dt * (kinetic + potential)



@njit 
def transition_amp(start,end,t,T,lambd,k):
    coeff = np.linspace(-5,5,40) # chosen precision of oscillatory sin
    trans_amp = 0.0
    for i in coeff:
        for j in coeff:
            for l in coeff:
                path = pathgrid(start,end,t,T,i,j,l)
                trans_amp = trans_amp + np.exp(-total_action(path,T,lambd,k))
    return trans_amp
@njit
def wavefunc(A,num,T,lambd,k):
    A_arr = np.linspace(-A,A,num)
    t = np.linspace(0,15,1500)
    
    trans_arr = np.empty_like(A_arr)

    for i in range(len(A_arr)): 
        
        trans_arr[i]=transition_amp(0.0,A_arr[i],t,T,lambd,k)
    return A_arr,trans_arr # squared trans_arr is probability density

def wavefuncViz(A,num,ax):
    A_arr,prob_dens=wavefunc(A,num,T,lambd,k)
    ax.plot(A_arr,prob_dens**2,label = str(num)+' transition amplitudes')

def vizPath(start,end,t,T,a,b,c):
    path = pathgrid(start,end,t,T,a,b,c)
    fig,ax = plt.subplots()
    ax.plot(t,path)
    ax.plot(t,np.linspace(start,end,len(t)),linestyle = '--',color = 'black',label='Classical Path')
    ax.legend()
    ax.set_xlabel('t')
    ax.set_ylabel("A(t)")
    ax.set_xlim([0,15])
    ax.set_ylim([-5,5])
    dict = {'a':a,'b':b,'c':c}
    ax.set_title("Path of A=0 to A="+str(end)+" with Fourier Coefficients "+str(dict))
    plt.show()

def main():
    fig,ax = plt.subplots()
    ax.set_title(r"Wavefunction of Universe with $\Lambda=-1$ and k = 1")
    ax.set_xlabel("A")
    ax.set_ylabel(r'$|\psi(x)|^2$')
    # wavefuncViz(2,50,ax)
    wavefuncViz(2,50,ax)
    # wavefuncViz(2,25,ax)
  
    plt.legend()
    plt.show()
    
    # t = np.linspace(0,T,N)
    # a=0.5
    # b=1
    # c=2
    # vizPath(0,1,t,T,a,b,c)
    # vizPath(0,1,t,T,a-0.5,b+1,c-1)
if __name__=="__main__":
    main()
    