import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src'))
from u_xx_f_sympy import model2, x
import sympy as sym
import numpy as np
from fe1D import finite_element1D, mesh_uniform, u_glob
import matplotlib.pyplot as plt

C = 5
D = 2
L = 4

m_values = [0, 1, 2, 3, 4]
d_values = [1, 2, 3, 4]
for m in m_values:
    u = model2(x**m, L, C, D)
    print('\nm=%d, u: %s' % (m, u))
    u_exact = sym.lambdify([x], u)

    for d in d_values:
        vertices, cells, dof_map = mesh_uniform(
            N_e=2, d=d, Omega=[0,L], symbolic=False)
        vertices[1] = 3  # displace vertex
        essbc = {}
        essbc[dof_map[-1][-1]] = D

        c, A, b, timing = finite_element1D(
            vertices, cells, dof_map,
            essbc,
            ilhs=lambda e, phi, r, s, X, x, h:
            phi[1][r](X, h)*phi[1][s](X, h),
            irhs=lambda e, phi, r, X, x, h:
            x**m*phi[0][r](X),
            blhs=lambda e, phi, r, s, X, x, h: 0,
            brhs=lambda e, phi, r, X, x, h:
            -C*phi[0][r](-1) if e == 0 else 0,
            intrule='GaussLegendre')

        # Visualize
        # (Recall that x is a symbol, use xc for coordinates)
        xc, u, nodes = u_glob(c, vertices, cells, dof_map)
        u_e = u_exact(xc)
        print('Max diff at nodes, d=%d:' % d, \
              np.abs(u_exact(nodes) - c).max())
        plt.figure()
        plt.plot(xc, u, 'b-', xc, u_e, 'r--')
        plt.legend(['finite elements, d=%d' %d, 'exact'],
                   loc='lower left')
        figname = 'tmp_%d_%d' % (m, d)
        plt.savefig(figname + '.png'); plt.savefig(figname + '.pdf')
    for ext in 'pdf', 'png':
        cmd = 'doconce combine_images -2 '
        cmd += ' '.join(['tmp_%d_%d.' % (m, d) + ext
                         for d in d_values])
        cmd += ' u_xx_xm%d_P1to4.' % m + ext
        print(cmd)
        os.system(cmd)

#plt.show()
