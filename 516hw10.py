import numpy as np
import matplotlib.pyplot as plt

def signal(t,f1,f2):
    arg1 = 2*np.pi*f1*t
    arg2 = 2*np.pi*f2*t
    return np.sin(arg1)+0.5*np.sin(arg2)

def vary_T():
    T = [1,1.25,1.5,1.75,2,3]
    N = 256


    fig,ax = plt.subplots(len(T),figsize=(10,8))
    for i,j in enumerate(T):
        t = np.linspace(0, j, N)
        sampled = signal(t, 5, 6)
        fft_sampled = np.fft.fft(sampled)
        fft_norm = np.abs(fft_sampled)
        frequencies = np.fft.fftfreq(N,j)
        ax[i].plot(frequencies,fft_norm)
        ax[i].set_xlim((0,0.25))
        ax[i].set_title('T = '+str(j))
    fig.tight_layout()
    plt.show()
def vary_N():
    T = 10
    N = [256,512,1024,2048,5096]

    fig, ax = plt.subplots(len(N), figsize=(10, 8))
    for i, j in enumerate(N):
        t = np.linspace(0, T, j)
        sampled = signal(t, 5, 6)
        fft_sampled = np.fft.fft(sampled)
        fft_norm = np.abs(fft_sampled)
        frequencies = np.fft.fftfreq(j, T)
        ax[i].plot(frequencies, fft_norm)
        ax[i].set_xlim((0, 0.25))
        ax[i].set_title('N = ' + str(j))
    fig.tight_layout()
    plt.show()

def main():
    vary_T()
    vary_N()
if __name__ == '__main__':
    main()