import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src-approx'))
from fe_approx1D_numint import approximate, mesh_uniform, u_glob
from sympy import sqrt, exp, sin, Symbol, lambdify, simplify
import numpy as np
from math import log

x = Symbol('x')
A = 1
w = 1

cases = {'sqrt': {'f': sqrt(x), 'Omega': [0,1]},
         'exp': {'f': A*exp(-w*x), 'Omega': [0, 3.0/w]},
         'sin': {'f': A*sin(w*x), 'Omega': [0, 2*np.pi/w]}}

results = {}
d_values = [1, 2, 3, 4]

for case in cases:
    f = cases[case]['f']
    f_func = lambdify([x], f, modules='numpy')
    Omega = cases[case]['Omega']
    results[case] = {}
    for d in d_values:
        results[case][d] = {'E': [], 'h': [], 'r': []}
        for N_e in [4, 8, 16, 32, 64, 128]:
            try:
                c = approximate(
                    f, symbolic=False,
                    numint='GaussLegendre%d' % (d+1),
                    d=d, N_e=N_e, Omega=Omega,
                    filename='tmp_%s_d%d_e%d' % (case, d, N_e))
            except np.linalg.linalg.LinAlgError as e:
                print str(e)
                continue
            vertices, cells, dof_map = mesh_uniform(
                N_e, d, Omega, symbolic=False)
            xc, u, _ = u_glob(c, vertices, cells, dof_map, 51)
            e = f_func(xc) - u
            # Trapezoidal integration of the L2 error over the
            # xc/u patches
            e2 = e**2
            L2_error = 0
            for i in range(len(xc)-1):
                L2_error += 0.5*(e2[i+1] + e2[i])*(xc[i+1] - xc[i])
            L2_error = np.sqrt(L2_error)
            h = (Omega[1] - Omega[0])/float(N_e)
            results[case][d]['E'].append(L2_error)
            results[case][d]['h'].append(h)
        # Compute rates
        h = results[case][d]['h']
        E = results[case][d]['E']
        for i in range(len(h)-1):
            r = log(E[i+1]/E[i])/log(h[i+1]/h[i])
            results[case][d]['r'].append(round(r, 2))

print results
for case in results:
    for d in sorted(results[case]):
        print 'case=%s d=%d, r: %s' % \
              (case, d, results[case][d]['r'])
