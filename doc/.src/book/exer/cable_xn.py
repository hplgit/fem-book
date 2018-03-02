import os, sys
sys.path.insert(0, os.path.join(os.pardir, 'src'))
from varform1D import solver
import sympy as sym
x, b = sym.symbols('x b')
f = 1

# Compute basis functions and their derivatives
N = 4
psi = {0: [x**(i+1) for i in range(N+1)]}
psi[1] = [sym.diff(psi_i, x) for psi_i in psi[0]]

# Galerkin

def integrand_lhs(psi, i, j):
    return psi[1][i]*psi[1][j]

def integrand_rhs(psi, i):
    return -f*psi[0][i]

Omega = [0, 1]

u, c = solver(integrand_lhs, integrand_rhs, psi, Omega,
              verbose=True, symbolic=True)
print('Galerkin solution u:', sym.simplify(sym.expand(u)))

# Least squares
psi = {0: [x**(i+2) for i in range(N+1)]}
psi[1] = [sym.diff(psi_i, x) for psi_i in psi[0]]
psi[2] = [sym.diff(psi_i, x) for psi_i in psi[1]]

def integrand_lhs(psi, i, j):
    return psi[2][i]*psi[2][j]

def integrand_rhs(psi, i):
    return -f*psi[2][i]

Omega = [0, 1]

u, c = solver(integrand_lhs, integrand_rhs, psi, Omega,
              verbose=True, symbolic=True)
print('solution u:', sym.simplify(sym.expand(u)))
