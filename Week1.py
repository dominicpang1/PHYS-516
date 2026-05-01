import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


# r = 1

def colatitude():
    return math.acos(2*random.random()-1)


def azimuthal():
    return random.random() * np.pi * 2


def generateCoords(num):
    x = []
    y = []
    z = []
    for i in range(num):
        phi = colatitude()
        theta = azimuthal()
        x.append(math.sin(phi) * math.cos(theta))
        y.append(math.sin(phi) * math.sin(theta))
        z.append(math.cos(phi))
    return x,y,z

#ts proolly ahh 
def rejection_coord(num):
    in_sphere = True
    x=[]
    y=[]
    z=[]
    for i in range(num):
        a = random.random()*2-1
        b = random.random()*2-1
        c = random.random()*2-1
        r = math.sqrt(a*a+b*b+c*c)
        x.append(a/r)
        y.append(b/r)
        z.append(c/r)
    return x,y,z

def main():
    x, y, z = generateCoords(750)

    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')

    ax.plot(0,0,np.linspace(-1,1))
    ax.set_box_aspect((1, 1, 1))
    #plt.show()

    a,b,c = rejection_coord(750)
   # ax.scatter(a, b, c, c='b', marker='o')
    plt.show()

if __name__ == '__main__':
    main()
