import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

#takes in wavefunc at all points, a Nx2 array
# a is change in x position between points, related to # of points
def F(psi,x):
    R = np.array(psi[:,0])
    I = np.array(psi[:,1])
    step = x[1]-x[0]
    #add the boundary conditions
    R_boundary = np.concatenate([[0],R,[0]])
    I_boundary = np.concatenate([[0],I,[0]])
    dR_dt = []
    dI_dt = []
    for i in range(1,len(R_boundary)-1):
        dR_dt.append((-0.5*(I_boundary[i+1]-(2*I_boundary[i])+I_boundary[i-1])/(step**2))+(0.5*I_boundary[i]*x[i-1]**2))
        dI_dt.append((0.5*(R_boundary[i+1]-(2*R_boundary[i])+R_boundary[i-1])/(step**2))-(0.5*R_boundary[i]*x[i-1]**2))
    k = np.array([dR_dt, dI_dt])    # 2 by N matrix.
    return np.transpose(k)
    # returns N by 2 , which is same structure as psi

def get_next_point(psi,t_step,x):
    #k's must have same structure as psi
    k1 = t_step*F(psi,x)
    k2 = t_step*F(psi+k1/2,x)
    k3 = t_step*F(psi+k2/2,x)
    k4 = t_step*F(psi+k3,x)
    psi_new = psi + (k1/6) + (k2/3) + (k3/3) + (k4/6)
    return psi_new

#fig = plt.figure(figsize=(8.8))



# def evolve(x,t):
#
#     x_range = x
#     t_range = t
#     t_step = t_range[1]-t_range[0]
#     initial_R_list = []
#     for i in x_range:
#         if i >= -0.5 and i <=0.5:
#             initial_R_list.append(1)
#         else:
#             initial_R_list.append(0)
#     initial_R = np.array(initial_R_list)
#     initial_I = np.zeros_like(initial_R)
#     psi_initial = np.transpose(np.array([initial_R,initial_I]))
#
#     psi_evolution = [psi_initial]
#
#     for i in range(1,len(t_range)):
#         psi_evolution.append(get_next_point(psi_evolution[i-1],t_step,x_range))
#     return psi_evolution

def evolve(psi_initial,t_range,x_range):
    t_step = t_range[1]-t_range[0]
    psi_evolution = [psi_initial]
    for i in range(1,len(t_range)):
        psi_evolution.append(get_next_point(psi_evolution[i-1],t_step,x_range))
        print('evolution',int(100*i/len(t_range)),'% done')
    return psi_evolution


def simpson(x_range,function):
    points = x_range
    step = points[1]-points[0]
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + (1/3)*function[i]
        elif i%2==1:
            integral = integral + (4/3)*function[i]
        else:
            integral = integral + (2 / 3) * function[i]
    return step*integral
def trapezoid(x_range,function):

    points = x_range
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + 0.5*function[i]
        else:
            integral = integral + function[i]
    return (points[1]-points[0])*integral

def main():
    M = 10
    a = 0.01 # step
    N = int(2 * M / a) + 1
    x_range = np.linspace(-M, M, N)
    t_step = 0.0001
    t_end = 5#4 * np.pi
    N_t = int(t_end / t_step) + 1
    t_range = np.linspace(0, t_end, N_t)
    initial_R_list = []
    for i in x_range:
        if i >= -0.5 and i <= 0.5:
            initial_R_list.append(1)
        else:
            initial_R_list.append(0)
    initial_R = np.array(initial_R_list)
    initial_I = np.zeros_like(initial_R)
    psi_initial = np.transpose(np.array([initial_R, initial_I]))

    psi_evolution = evolve(psi_initial,t_range,x_range)

    times,spaces,complexes = np.shape(psi_evolution)

    psi_mag = np.zeros([times,spaces])

    for i,j in enumerate(psi_evolution):
        for ii,jj in enumerate(j):
            psi_mag[i][ii] = jj[0]**2 + jj[1]**2

    #fig = plt.figure(figsize=(8.8))
    total_probability_trap = []
    for i,j in enumerate(t_range):
        total_probability_trap.append(trapezoid(x_range, psi_mag[i]))
        print('integration',100.0*j/t_end,'% done')
    plt.plot(t_range, total_probability_trap, label="time evolution of total probability in the range -M to M")
    plt.legend()
    plt.xlim([0, t_end])
    plt.ylim([0, 2])
    plt.grid()
    plt.show()
    #print(total_probability_trap[0])


    for i in range(len(psi_evolution)):
        #plt.plot(x_range,psi_evolution[i][:,0],label = "Real Comp at time: "+str(t_range[i]))
        #plt.plot(x_range,psi_evolution[i][:,1],label = "Imaginary comp at time "+str(t_range[i]))
        plt.plot(x_range,psi_mag[i],label = "magnitude of wave function at time: "+str(t_range[i]))
        plt.legend()
        plt.xlim([-15, 15])
        plt.ylim([-2, 2])
        plt.show()



    # Nt, Nx = psi_mag.shape
    # fig, ax = plt.subplots()
    # line, = ax.plot(x_range, psi_mag[0])
    #
    # ax.set_xlim(-M, M)
    # ax.set_ylim(0, psi_mag.max())
    # ax.set_xlabel("x")
    # ax.set_ylabel("|ψ(x,t)|")
    #
    # def update(frame):
    #     line.set_ydata(psi_mag[frame])
    #     return line,
    # frames = np.arange(0,Nt,20)
    # ani = FuncAnimation(fig, update, frames=frames, interval=30)
    #
    # ani.save("wavefunction.gif", writer=PillowWriter(fps=30))
if __name__ == '__main__':
    main()