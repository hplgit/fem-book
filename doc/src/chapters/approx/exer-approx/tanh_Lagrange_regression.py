import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src-approx'))
from approx1D import regression, comparison_plot
from Lagrange import Lagrange_polynomials
import sympy as sym
import numpy as np

x = sym.Symbol('x')
Omega = [0,1]
N_values = 3, 7, 11, 15

for s in 5, 20:
    f = -sym.tanh(s*(x-0.5))  # sympy expression
    for distribution in 'uniform', 'Chebyshev':
        for N in N_values:
            # Compute the points from a 2*N Lagrange polynomial
	    dummy, points = Lagrange_polynomials(
                x, 2*N, Omega,
                point_distribution=distribution)
            # Compute phi from N points Lagrange polynomial
	    phi, dummy = Lagrange_polynomials(
                x, N, Omega,
                point_distribution=distribution)
            points = np.array(points, dtype=float)
            point_values = -np.tanh(s*(points-0.5))

	    u, c = regression(f, phi, points)
	    filename = 'tmp_tanh_%d_%d_%s' % (N, s, distribution)
	    comparison_plot(f, u, Omega, filename,
			    plot_title='s=%g, N=%d, %s points' %
			    (s, N, distribution),
                            points=points, point_values=point_values,
                            points_legend='%s points' % (2*N))
        # Combine plot files (2x2)
        for ext in 'png', 'pdf':
            cmd = 'doconce combine_images ' + ext + ' '
            cmd += ' '.join([
                'tmp_tanh_%d_%d_%s' % (N, s, distribution)
                for N in N_values])
            cmd += ' tanh_Lagrange_regr_%s_s%s' % (distribution, s)
            os.system(cmd)
