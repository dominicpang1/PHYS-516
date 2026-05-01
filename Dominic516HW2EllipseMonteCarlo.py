import random
import numpy as np
import matplotlib.pyplot as plt

def ellipse_area(a,b,N):
    count = 0
    for i in range(N):
        x = random.random()*2*a-a
        y = random.random()*2*b-b
        if ((x/a)**2)+((y/b)**2)<=1:
            count = count+1
    return count/N * 4*a*b

def estimate(n,m):
    a=2
    b=5
    area_list = []
    for i in range(m):
        area_list.append(ellipse_area(a,b,n))
    #area = np.mean(np.array(area_list))
    #print("Area of ellipse:",area)
    standard_error = np.std(area_list)/np.sqrt(m)
    #print("Standard Error of the Mean (uncertainty):",standard_error)
    return standard_error

def main():
    #fix N increase M
    #m_list = [10, 10,10,10,10, 50,50,50,50 ,100,100,100,100 ,500,500,500]
    #N = 10000
    ##uncertainty = []
    #for i, j in enumerate(m_list):
     #   uncertainty.append(estimate(N,j))
    #plt.scatter(m_list,uncertainty,label = "Fix points, Vary trials")
    #plt.title("Fix number of points, vary number of trials")
    #plt.xlabel("Number of trials")
    #plt.ylabel("Error")
    #plt.show()
    #increase # of trials: increase error - more spread? but it levels off

    #fix N increae M
    n_list = [10,100,1000,10000,100000]
    m = 15
    uncertainty = []
    for i,j in enumerate(n_list):
        uncertainty.append(estimate(j,m))
    plt.scatter(n_list, uncertainty, label="Fix trials, Vary points")
    plt.title("Fix trials, vary number of points")
    plt.xlabel("Number of points")
    plt.ylabel("Error")
    plt.show()
  #increase # of points - decrease error, inverse relationship

if __name__ == '__main__':
    main()