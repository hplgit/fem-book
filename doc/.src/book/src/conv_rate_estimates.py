from scipy import *
import sympy as sym
from approx1D import *
import pylab

Ns =[2, 4, 8, 16]
Taylor=[0.098338940295605456,0.0026365495198570031, 7.8308472693030405e-07, 3.5761786201094212e-10]
sinesoidal=[0.0027171077732842785,0.00061860119289018926,0.00011973410883625029,2.1735285579352844e-05]
Bernstein=[0.002128192258704093,4.4564352309826328e-05,8.7393355622010712e-09,4.4955566291096638e-15]
Lagrange=[0.0021281922587041003, 4.4564352309852179e-05, 8.7393355595603748e-09, 2.4560511714792771e-12]


x = sym.Symbol('x')

psi = [1, x]


u, c = regression_with_noise(log2(sinesoidal), psi, log2(Ns))
print u, c 

X = log2(Ns)
U = sym.lambdify([x], u)
UU = U(X) 

pylab.plot(X, log2(sinesoidal))
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


  

