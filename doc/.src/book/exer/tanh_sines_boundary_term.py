import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src'))
import sympy as sym
from approx1D import least_squares_orth, comparison_plot
import matplotlib.pyplot as plt
x = sym.Symbol('x')

def efficient(f, B, s, Omega, N=10, basis='a'):
    u = B
    for i in range(N+1):
        if basis == 'a':
            psi = [sym.sin((i+1)*x)]
        elif basis == 'b':
            psi = [sym.sin((2*i+1)*x)]
        elif basis == 'c':
            psi = [sym.sin(2*(i+1)*x)]
        next_term, c = least_squares_orth(f-B, psi, Omega, False)
        u = u + next_term
        # Make only plot for i even
        if i % 2 == 0:
            comparison_plot(f, u, Omega, 'tmp_sin%02dx' % i,
                            legend_loc='upper left', show=False,
                            plot_title='s=%g, i=%d' % (s, i))


if __name__ == '__main__':
    s = 20  # steepness
    f = sym.tanh(s*(x-sym.pi))
    from math import pi
    Omega = [0, 2*pi]  # sym.pi did not work here

    # sin((i+1)*x) basis
    xL = Omega[0]
    xR = Omega[1]
    B = ((xR-x)*f.subs(x, xL) + (x-xL)*f.subs(x, xR))/(xR-xL)
    for exercise in 'a', 'b', 'c':
        efficient(f, B, s, Omega, N=16, basis=exercise)
        # Make movie
        cmd = 'convert -delay 200 tmp_sin*.png '
        cmd += 'tanh_sines_boundary_term_%s.gif' % exercise
        os.system(cmd)
        # Make static plots, 3 figures on 2 lines
        for ext in 'pdf', 'png':
            cmd = 'doconce combine_images %s -3 ' % ext
            cmd += 'tmp_sin00x tmp_sin02x tmp_sin04x tmp_sin08x '
            cmd += 'tmp_sin12x tmp_sin16x '
            cmd += 'tanh_sines_boundary_term_%s' % exercise
            os.system(cmd)

