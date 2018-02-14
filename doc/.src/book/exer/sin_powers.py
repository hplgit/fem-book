import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src'))
import sympy as sym
from approx1D import least_squares, comparison_plot
from math import pi
import matplotlib.pyplot as plt

x = sym.Symbol('x')
f = sym.sin(x)
N = 7
psi_bases = [[x**i for i in range(1, N+1, 2)],  # V_1
             [x**i for i in range(0, N+1)]]     # V_2
symbolic = False

for V, psi in enumerate(psi_bases):
    for domain_no in range(1, 3):
        for k in range(2, 6):
            if symbolic:
                Omega = [0, k*sym.pi] if domain_no == 1 else \
                        [-k*sym.pi/2, k*sym.pi/2]
            else:
                # cannot use sym.pi with numerical sympy computing
                Omega = [0, k*pi] if domain_no == 1 else \
                        [-k*pi/2, k*pi/2]

            u, c = least_squares(f, psi, Omega, symbolic=symbolic)

            comparison_plot(
                f, u, Omega,
                ymin=-2, ymax=2,
                filename='tmp_N%d_V%dOmega%dk%d' %
                (N, V, k, domain_no),
                plot_title='sin(x) on [0,%d*pi/2] by %s' %
                (k, ','.join([str(p) for p in psi])))
            # Need to kill the plot to proceed!
        for ext in 'png', 'pdf':
            cmd = 'doconce combine_images -2 ' + \
                  ' '.join(['tmp_N%d_V%dOmega%dk%d.' %
                            (N, V, k, domain_no) + ext
                            for k in range(2, 6)]) + \
                  ' sin_powers_N%d_V%d_Omega%d.' % (N, V, domain_no) + ext
            print(cmd)
            os.system(cmd)

# Show the standard Taylor series approximation
from math import factorial, pi
import time
Omega = [0, 12*pi/2.]
u = 0
for k in range(0,N+1):
    u = u + ((-1)**k*x**(1+2*k))/float(factorial(1+2*k))
# Shorter: u = sum(((-1)**k*x**(1+2*k))/float(factorial(1+2*k))
# for k in range(0,10))
comparison_plot(f, u, Omega, 'sin_taylor%d' % k,
                ymin=-1.5, ymax=1.5)
