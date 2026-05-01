import numpy as np
import matplotlib.pyplot as plt

def simpson(x_range,function):
    points = x_range
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + (1/3)*function[i]
        elif i%2==1:
            integral = integral + (4/3)*function[i]
        else:
            integral = integral + (2/3) * function[i]
    return (points[1]-points[0])*integral
def trapezoid(x_range,function):
    points = x_range
    integral = 0
    for i,j in enumerate(points):
        if i == 0 or i == len(points)-1:
            integral = integral + 0.5*function[i]
        else:
            integral = integral + function[i]
    return (points[1]-points[0])*integral

M = 10
a = 0.1  # step
N = int(2 * M / a) + 1
x_range = np.linspace(-M, M, N)
t_step = 0.01
t_end = 4 * np.pi
N_t = int(t_end / t_step) + 1
t_range = np.linspace(0, t_end, N_t)
initial_R_list = []
for i in x_range:
    if i >= -0.5 and i <=0.5:
        initial_R_list.append(1)
    else:
        initial_R_list.append(0)
initial_R = np.array(initial_R_list)
initial_I_list = [0 for i in range(len(initial_R_list))]
print("Length of R:", len(initial_R_list))
print("Length of I:", len(initial_I_list))
print("Lenght of list:",len(x_range))
initial_mag = [i**2 + j**2 for i,j in zip(initial_R_list,initial_I_list)]
plt.plot(x_range,initial_mag)
plt.show()

initial_prob =  trapezoid(x_range,initial_mag)
initial_prob_simp = simpson(x_range,initial_mag)
print(initial_mag)
print("trapezoid integral:",initial_prob)
print("simpson integral:", initial_prob_simp)