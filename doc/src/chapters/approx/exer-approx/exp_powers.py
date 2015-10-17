import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src-approx'))
from approx1D import least_squares, comparison_plot
import matplotlib.pyplot as plt
import sympy as sym
from math import factorial
import numpy as np

x = sym.Symbol('x')
f = sym.exp(-x)

Omega = [0, 8]

for N in 2,4,6:
    psi = [x**i for i in range(N+1)]
    u, c = least_squares(f,psi,Omega)
    print N, u
    plt.figure()
    comparison_plot(f, u, Omega, filename='tmp_exp_%d' % N,
                    plot_title='N=%d' % N)
