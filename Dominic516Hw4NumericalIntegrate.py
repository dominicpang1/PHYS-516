import numpy as np
import matplotlib.pyplot as plt

def Func(x,y,z):
    sigma = 1
    r = np.sqrt((x*x)+(y*y)+(z*z))
    return sigma/r

def potential_integrator_trap(upper,lower,function):

    points = np.linspace(lower,upper,len(function))
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + 0.5*function[i]
        else:
            integral = integral + function[i]
    return (points[1]-points[0])*integral
def potential_integrator_simpson(upper,lower,function):
    points = np.linspace(lower, upper, len(function))
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + (1/3)*function[i]
        elif i%2==1:
            integral = integral + (4/3)*function[i]
        else:
            integral = integral + (2 / 3) * function[i]
    return (points[1]-points[0])*integral

def main():
    z = np.linspace(0.01,10,50)
    phi_trap = []
    phi_simp = []
    sentinel = True
    previous_trap = 0
    previous_simp = 0
    x_step = 0.01
    while sentinel:
        for a in z:
            R = 1
            x = np.linspace(-R, R , int(2/x_step))
            y2 = np.sqrt(1 - x ** 2)
            y1 = -1 * y2

            G_trap = []
            G_simp = []
            for i,j in enumerate(x):
                G_trap.append(potential_integrator_trap(y2[i],y1[i],Func(j,np.linspace(y1[i],y2[i],len(x)),a)))
                G_simp.append(potential_integrator_simpson(y2[i],y1[i],Func(j,np.linspace(y1[i],y2[i],len(x)),a)))
            phi_trap.append(potential_integrator_trap(R,-R,G_trap))
            phi_simp.append(potential_integrator_simpson(R,-R,G_simp))
            print(len(phi_trap))
        if np.abs(phi_trap[0]-previous_trap) > 0.01:
            previous_trap = phi_trap[0]
            x_step = x_step/2
            phi_trap = []
            phi_simp = []
        else:
            sentinel = False


    plt.plot(z,phi_trap,label = "trapezoidal integration")
    plt.plot(z,phi_simp,label = "simpson integration")
    plt.xlabel('z')
    plt.ylabel('Potential')
    print(z)
    print("Trapezoidal",phi_trap)
    print("Simpson",phi_simp)

    plt.show()
if __name__ == '__main__':
    main()