"""
3D version of approx2D.py.
Numerical integration only.
"""
import sympy as sym
import numpy as np
import scipy.integrate

def least_squares(f, psi, Omega):
    """
    Given a function f(x,y,z) on a rectangular domain
    Omega=[[xmin,xmax],[ymin,ymax],[zmin,zmax]],
    return the best approximation to f in the space V
    spanned by the functions in the list psi.
    f and psi are symbolic (sympy) expressions, but will
    be converted to numeric functions for faster integration.
    """
    N = len(psi) - 1
    A = np.zeros((N+1, N+1))
    b = np.zeros(N+1)
    x, y, z = sym.symbols('x y z')
    f = sym.lambdify([x, y, z], f, modules='numpy')
    psi_sym = psi[:]  # take a copy, needed for forming u later
    psi = [sym.lambdify([x, y, z], psi[i]) for i in range(len(psi))]

    print('...evaluating matrix...')
    for i in range(N+1):
        for j in range(i, N+1):
            print('(%d,%d)' % (i, j))

            integrand = lambda x, y, z: psi[i](x,y,z)*psi[j](x,y,z)
            I, err = scipy.integrate.nquad(
                integrand,
                [[Omega[0][0], Omega[0][1]],
                 [Omega[1][0], Omega[1][1]],
                 [Omega[2][0], Omega[2][1]]])
            A[i,j] = A[j,i] = I
        integrand = lambda x, y, z: psi[i](x,y,z)*f(x,y,z)
        I, err = scipy.integrate.nquad(
            integrand,
            [[Omega[0][0], Omega[0][1]],
             [Omega[1][0], Omega[1][1]],
             [Omega[2][0], Omega[2][1]]])
        b[i] = I
    print()
    c = np.linalg.solve(A, b)
    if N <= 10:
        print('A:\n', A, '\nb:\n', b)
        print('coeff:', c)
    u = sum(c[i]*psi_sym[i] for i in range(len(psi_sym)))
    print('approximation:', u)
    return u, c

def sine_basis(Nx, Ny, Nz):
    """
    Compute basis sin((p+1)*pi*x)*sin((q+1)*pi*y)*sin((r+1)*pi*z),
    p=0,...,Nx, q=0,...,Ny, r=0,...,Nz.
    """
    x, y, z = sym.symbols('x y z')
    psi = []
    for r in range(0, Nz+1):
        for q in range(0, Ny+1):
            for p in range(0, Nx+1):
                s = sym.sin((p+1)*sym.pi*x)*\
                    sym.sin((q+1)*sym.pi*y)*sym.sin((r+1)*sym.pi*z)
                psi.append(s)
    return psi

def test_least_squares():
    # Use sine functions
    x, y, z = sym.symbols('x y z')
    N = 1  # (N+1)**3 = 8 basis functions
    psi = sine_basis(N, N, N)
    f_coeff = [0]*len(psi)
    f_coeff[3] = 2
    f_coeff[4] = 3
    f = sum(f_coeff[i]*psi[i] for i in range(len(psi)))
    # Check that u exactly reproduces f
    u, c = least_squares(f, psi, Omega=[[0,1], [0,1], [0,1]])
    diff = np.abs(np.array(c) - np.array(f_coeff)).max()
    print('diff:', diff)
    tol = 1E-15
    assert diff < tol

if __name__ == '__main__':
    import time
    t0 = time.clock()
    test_least_squares()
