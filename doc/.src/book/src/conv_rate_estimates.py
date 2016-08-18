from scipy import *
import sympy as sym
from approx1D import *
import pylab

Ns =[2, 4, 8, 16]
Taylor     = [0.0983, 0.00263,  7.83e-07, 3.57e-10]
Sinusoidal = [0.0027, 0.00061,  0.00012,  2.17e-05]
Bernstein  = [0.0021, 4.45e-05, 8.73e-09, 4.49e-15]
Lagrange   = [0.0021, 4.45e-05, 8.73e-09, 2.45e-12]


x = sym.Symbol('x')
psi = [1, x]

u, c = regression_with_noise(log2(Sinusoidal), psi, log2(Ns))
print u, c 

X = log2(Ns)
U = sym.lambdify([x], u)
UU = U(X) 

pylab.plot(X, log2(Sinusoidal))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()


u, c = regression_with_noise(log(Bernstein), psi, Ns)
print u, c 

X = Ns
U = sym.lambdify([x], u)
UU = U(array(X)) 

pylab.plot(X, log(Bernstein))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()


u, c = regression_with_noise(log(Taylor), psi, Ns)
print u, c 

X = Ns
U = sym.lambdify([x], u)
UU = U(array(X)) 

pylab.plot(X, log(Taylor))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()

u, c = regression_with_noise(log(Lagrange), psi, Ns)
print u, c 

X = Ns
U = sym.lambdify([x], u)
UU = U(array(X)) 

pylab.plot(X, log(Lagrange))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()



 

