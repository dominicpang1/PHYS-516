import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# a = x
# c = y

def func(x,y):
    return x**2+y**2

def grad(x,y):

    return 2*x,2*y


def get_next(x0,y0,step):
    dx,dy= grad(x0,y0)
    x = x0 - step*dx
    y = y0 - step* dy
    return x,y

def main():
    i,j = 2,2
    initial_E = func(i,j)
    min_E = 10000
    print(initial_E)
    x_s=[i]
    y_s=[j]
    diff = 1
    count = 0
    while diff > 0.0001:
        initial_E = func(i,j)
        x,y = get_next(i,j,0.1)
        min_E = func(x,y)
        x_s.append(x)
        y_s.append(y)
        i,j = x,y
        diff = np.abs(min_E - initial_E)
        count = count+1
    print("(a,c):",i,j)
    print(min_E)
    print(func(1,0))
    print("Count:",count)

    # plotx = np.linspace(-2,2,100)
    # ploty = np.linspace(-2,2,100)
    #
    # Egrid =np.zeros((len(plotx),len(ploty)))
    # for i in range(len(plotx)):
    #     for j in range(len(ploty)):
    #         Egrid[i][j]= func(plotx[i],ploty[j])
    #
    # fig, ax = plt.subplots()
    # sns.heatmap(Egrid)
    # plt.plot(plotx,ploty,color = 'white')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()

if __name__ == "__main__":
    main()