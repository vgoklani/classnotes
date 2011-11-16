import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(t,A,k,K):
    return K / (1+A*np.exp(-k*t))    

def resid(p, y, t):
    A,k,K = p
    return y - f(t,A,k,K)

if __name__ == '__main__':
    #t, x1 = np.loadtxt('us.txt', unpack=True)
    t, x1 = np.loadtxt('world.txt', unpack=True)
    t = np.linspace(0,1,len(t))
    print t
    
    A0,k0,K0 = 1, 1, 1
    [A,k,K], flag  = optimize.leastsq(resid, [A0,k0,K0], args=(x1, t))

    print "flag",flag
    print "A", A
    print "k",k
    print "K",K
        
    t = np.linspace(0,4,len(t))    
    plt.plot(t, f(t,A,k,K), 'go')
    #plt.hold(True)            
    #plt.plot(t, x1, 'ro')
    
    
    plt.show()