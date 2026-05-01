import numpy as np
import matplotlib.pyplot as plt

def get_next_point(theta,omega,step):
    k1 = step*np.array((omega,-np.sin(theta)))
    k2 = step*np.array((omega+0.5*k1[1],-np.sin(theta+0.5*k1[0])))
    k3 = step*np.array((omega+0.5*k2[1],-np.sin(theta+0.5*k2[0])))
    k4 = step*np.array((omega+k3[1],-np.sin(theta+k3[0])))
    theta_next = theta + (1/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
    omega_next = omega + (1/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    return theta_next,omega_next


def runge_kutta_evolve(start, stop,initial_cond,initial_step):
    previous = 0
    t = np.linspace(start,stop,int((stop-start)/initial_step+1))
    initial = initial_cond
    theta = []
    for i in t:
        initial = get_next_point(initial[0],initial[1],initial_step)
        theta.append(initial[0])
    diff = np.abs(previous - theta[-1])
    previous_step = initial_step
    while diff>0.01:
        previous = theta[-1]
        previous_step = previous_step/2
        initial = initial_cond
        theta = []
        t = np.linspace(start, stop, int((stop - start) / previous_step + 1))
        for i in t:
            initial = get_next_point(initial[0], initial[1], previous_step)
            theta.append(initial[0])
        diff = np.abs(previous - theta[-1])
    print("Final Stepsize:",previous_step)
    plt.plot(t,theta)
    plt.show()
    return theta

def main():
    theta = runge_kutta_evolve(0,10,(np.pi/3,0),1)

if __name__ == '__main__':
    main()