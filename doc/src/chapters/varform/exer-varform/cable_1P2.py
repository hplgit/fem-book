import sympy as sym
X, h = sym.symbols('X h')
half = sym.Rational(1, 2)
psi = [half*(X-1)*X, 1-X**2, half*(X+1)*X]
dpsi_dX = [sym.diff(psi[r], X) for r in range(len(psi))]

# Element matrix
# (2/h)*dpsi_dX[r]*(2/h)*dpsi_dX[s]*h/2
import numpy as np
d = 2
# Use a numpy matrix with general objects to hold A
A = np.empty((d+1, d+1), dtype=object)
for r in range(d+1):
    for s in range(d+1):
        integrand = dpsi_dX[r]*dpsi_dX[s]*2/h
        A[r,s] = sym.integrate(integrand, (X, -1, 1))
print A

# Element vector
# f*psi[r]*h/2, f=1
d = 2
b = np.empty(d+1, dtype=object)
for r in range(d+1):
    integrand = -psi[r]*h/2
    b[r] = sym.integrate(integrand, (X, -1, 1))
print b
