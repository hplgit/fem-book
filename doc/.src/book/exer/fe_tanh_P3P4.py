import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src'))
from fe_approx1D_numint import approximate, u_glob
from sympy import tanh, Symbol, lambdify
x = Symbol('x')

steepness = 20
arg = steepness*(x-0.5)

approximate(tanh(arg), symbolic=False, numint='GaussLegendre4',
            d=3, N_e=1, filename='fe_p3_tanh_1e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre4',
            d=3, N_e=2, filename='fe_p3_tanh_2e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre4',
            d=3, N_e=4, filename='fe_p3_tanh_4e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre5',
            d=4, N_e=1, filename='fe_p4_tanh_1e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre5',
            d=4, N_e=2, filename='fe_p4_tanh_2e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre5',
            d=4, N_e=4, filename='fe_p4_tanh_4e')

# Interpolation method
import numpy as np
import matplotlib.pyplot as plt
f = lambdify([x], tanh(arg), modules='numpy')

# Compute exact f on a fine mesh
x_fine = np.linspace(0, 1, 101)
f_fine = f(x_fine)

for d in 3, 4:
    for N_e in 1, 2, 4:
        h = 1.0/N_e  # element length
        vertices = [i*h for i in range(N_e+1)]
        cells = [[e, e+1] for e in range(N_e)]
        dof_map = [[d*e + i for i in range(d+1)] for e in range(N_e)]
        N_n = d*N_e + 1  # Number of nodes
        x_nodes = np.linspace(0, 1, N_n)  # Node coordinates
        U = f(x_nodes)  # Interpolation method samples node values
        x, u, _ = u_glob(U, vertices, cells, dof_map,
                         resolution_per_element=51)
        plt.figure()
        plt.plot(x, u, '-', x_fine, f_fine, '--',
                 x_nodes, U, 'bo')
        plt.legend(['%d P%d elements' % (N_e, d),
                    'exact', 'interpolation points'],
                   loc='upper left')
        plt.savefig('tmp_%d_P%d.pdf' % (N_e, d))
        plt.savefig('tmp_%d_P%d.png' % (N_e, d))
plt.show()

