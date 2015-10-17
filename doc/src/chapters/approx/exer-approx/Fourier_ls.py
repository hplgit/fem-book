import numpy as np
import matplotlib.pyplot as plt
from math import pi
from numpy import sin

def Heaviside_series(x, N):
    s = 0.5
    for k in range(N):
        s += -2.0/((2*k+1)*pi)*sin(2*(2*k+1)*pi*x)
    return s

x = np.linspace(0, 1, 1001)
for N in 5, 100:
    H = Heaviside_series(x, N)
    plt.figure()
    plt.plot(x, H)
    plt.legend(['$N=%d$' % N], loc='upper left')
    plt.savefig('tmp_%d.png' % N)
    plt.savefig('tmp_%d.pdf' % N)
plt.show()

