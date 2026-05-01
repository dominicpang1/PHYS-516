import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#r = 1 

def colatitude(): 
    return random.random()*np.pi
def azimuthal():
    return random.random()*np.pi*2


def generateCoords(num):
    
    phi = np.array([])
    theta = np.array([])
    for i in range(num):
        np.append(phi,colatitude()) 
        np.append(theta,azimuthal())
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)
    return x,y,z

def main():
    x,y,z = generateCoords(100)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z,c='r',marker = 'o')
    plt.show()

if __name__ == '__main__':
    main()
