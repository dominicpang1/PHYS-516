import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def update_position(i,j,k):
    choice = random.randrange(0,6)
    if choice%2 == 0: #even, increase
        if choice == 0:
            i = i+1
        elif choice == 2:
            j = j + 1
        else:
            k = k + 1
    else:
        if choice == 1:
            i = i-1
        elif choice == 3:
            j= j-1
        else:
            k = k-1
    return i,j,k
def plotter(xp,yp,zp):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xp, yp, zp, c='r')
    ax.plot(0, 0, 0, c='r', marker='o', label='start')
    plt.legend()
    plt.show()


def main():

    N = [10,20,30,40,100,200,500,1000,2000,5000,7000,10000] # number of step
    M = 100 # averager
    average_distances = []
    for i in N:
        distance = []
        for k in range(M):
            x,y,z = 0,0,0
            for j in range(i-1):
                visited = [[x, y, z]]
                x_up,y_up,z_up = update_position(x,y,z)
                while [x_up,y_up,z_up] in visited:
                    x_up, y_up, z_up = update_position(x, y, z)
                x,y,z = x_up,y_up,z_up
                visited.append([x,y,z])
            final_point = np.array([x,y,z])
            distance.append(np.linalg.norm(final_point))
        average = np.average(distance)
        average_distances.append(average)

    fig,ax = plt.subplots()
    ax.scatter(N,average_distances)
    ax.set_title("number of random steps and average distance from origin")
    ax.set_xlabel("N")
    ax.set_ylabel("D")
    plt.show()
    # arr = np.array(visited)
    # xp = arr[:,0]
    # yp = arr[:,1]
    # zp = arr[:,2]
    # plotter(xp,yp,zp)



if __name__ == '__main__':
    main()