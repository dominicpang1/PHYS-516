import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# a = x
# c = y

def func(x,y):
    num = (x**2)*(9*y**2-6*x*y+2*x**4-4*x**3)
    den = 2*(45*y**2+12*y*x**2+2*x**4)
    return num/den

def grad(x,y):
    den = 4*(x**8)+48*y*(x**6)+324*(y**2)*(x**4)+1080*(x**2)*(y**3)+2025*(y**4)
    num_x = 4*(x**9)-4*(x**8)+48*y*(x**7)-66*y*(x**6)+252*(y**2)*(x**5)-486*(y**2)*(x**4)-405*(x**2)*(y**3)+405*x*(y**4)
    num_y = -12*(x**8)+18*(x**7)-72*y*(x**6)+180*y*(x**5)+54*(x**4)*(y**2)+135*(x**3)*(y**2)
    return num_x/den,num_y/den


def get_next(x0,y0,step):
    dx,dy= grad(x0,y0)
    x = x0 - step*dx
    y = y0- step* dy
    return x,y

def main():
    i,j = 1,1
    initial_E = func(i,j)
    min_E = 10000
    print(initial_E)
    x_s=[i]
    y_s=[j]
    diff = 1
    count = 0
    while diff > 0.00000001: #1e-6,1e-2
        initial_E = func(i,j)
        x,y = get_next(i,j,0.01)
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

    plotx = np.linspace(-2,2,100)
    ploty = np.linspace(-2,2,100)



    X, Y = np.meshgrid(plotx, ploty)
    Egrid = func(X,Y)
    fig, ax = plt.subplots()

    cont = ax.contourf(X, Y, Egrid, levels=50, cmap='viridis')
    cbar = fig.colorbar(cont, ax=ax)
    cbar.set_label("E(a,c)")
    ax.plot(x_s, y_s, color='red',lw=1)
    ax.plot(x_s[0],x_s[0],color='yellow',marker='o',label = "start")
    ax.plot(i,j,color='yellow',marker="*",label='end')
    ax.set_xlabel('a')
    ax.set_ylabel('c')
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()