import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src-approx'))
from approx1D import interpolation, comparison_plot
from Lagrange import Lagrange_polynomials
import sympy as sym

x = sym.Symbol('x')
Omega = [0,1]
N_values = 3, 7, 11, 15

for s in 5, 20:
    f = -sym.tanh(s*(x-0.5))  # sympy expression
    for distribution in 'uniform', 'Chebyshev':
        for N in N_values:
	    phi, points = Lagrange_polynomials(
                x, N, Omega,
                point_distribution=distribution)

	    u, c = interpolation(f, phi, points)
	    filename = 'tmp_tanh_%d_%d_%s' % (N, s, distribution)
	    comparison_plot(f, u, Omega, filename,
			    plot_title='s=%g, N=%d, %s points' %
			    (s, N, distribution))
        # Combine plot files (2x2)
        for ext in 'png', 'pdf':
            cmd = 'doconce combine_images ' + ext + ' '
            cmd += ' '.join([
                'tmp_tanh_%d_%d_%s' % (N, s, distribution)
                for N in N_values])
            cmd += ' tanh_Lagrange_%s_s%s' % (distribution, s)
            os.system(cmd)
