import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

randlist = []
for i in range (0,1000000):
    randlist.append(random.random())
n = 10000
plt.hist(randlist,n)
plt.title(str(n)+" Bins")
plt.ylabel("Count")
plt.xlabel("Value")
plt.show()

arr = np.array(randlist)

# values by hand or what 
mean = np.mean(arr)

var_arr = (arr-mean)**2
var = np.mean(var_arr)
# divide by n, not n-1 for total data, not sample
std = var**(1/2)

skew_arr = ((arr-mean)/std)**3
skew = np.mean(skew_arr)

kurt_arr = ((arr-mean)/std)**4
kurt = np.mean(kurt_arr)
print()
print("Data statistics for list of length",len(randlist))
print("Mean: ", mean)
print("Variance: ", var)
print("Skewness: ", skew)
print("Kurtosis: ", kurt)
print()

uni = np.linspace(0,1,1000000,endpoint = False) # don't make 1 an option
uni_mean = np.mean(uni)
uni_std = np.std(uni)
uni_var = uni_std**2
uni_skew_arr =  ((uni-uni_mean)/uni_std)**3
uni_skew = np.mean(uni_skew_arr)
uni_kurt_arr =  ((uni-uni_mean)/uni_std)**4
uni_kurt = np.mean(uni_kurt_arr)

# uniform values
# mean = 0.5 
# var = 0.083.. = 1/12 
# skew = 0
# kurt = 1.8

print()
print("Deviations from uniform for list of length",len(randlist))
print("deviation of mean:",np.abs(0.5-mean))
print("deviation of variance:",np.abs(1/12 - var))
print("deviation of skewness:",np.abs(skew))
print("deviation of kurtosis:",np.abs(1.8-kurt))
print()


#generating random sphere coords
#radius always same 

r = 1 

def colatitude(): 
    return random.random()*np.pi
def azimuthal():
    return random.random()*np.pi*2

coord = (1,azimuthal(),colatitude())

# rejection method - box and sphere
# this is worse because it uses cartesian
def rejection_coord(radius):
    in_sphere = True 
    while in_sphere:
        x = (random.random()*2) -1 
        y = (random.random()*2) -1 
        z = (random.random()*2) -1 
        if (x*x)+(y*y)+(z*z)==radius*radius: 
            in_sphere = False
            return (x,y,z)