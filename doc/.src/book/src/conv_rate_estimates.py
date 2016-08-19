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
print "estimated model for sine: %3.2e*N**(%3.2e)" % (2**(c[0]), c[1])
 
# check the numbers estimated by the model by manual inspection
for N in Ns: 
  print 2**c[0] * N **c[1]

X = log2(Ns)
U = sym.lambdify([x], u)
UU = U(X) 

pylab.plot(X, log2(Sinusoidal))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()

u, c = regression_with_noise(log(Bernstein), psi, Ns)
print "estimated model for Bernstein: %3.2e*exp(%3.2e*N)" % (exp(c[0]), c[1])

# check the numbers estimated by the model by manual inspection
for N in Ns: 
  print exp(c[0]) * exp(N * c[1])

X = Ns
U = sym.lambdify([x], u)
UU = U(array(X)) 

pylab.plot(X, log(Bernstein))
pylab.plot(X, UU)
pylab.legend(["data", "model"])
pylab.show()


CPU_Taylor    = [0.0123, 0.0325, 0.108,  0.441]
CPU_sine      = [0.0113, 0.0383, 0.229,  1.107]
CPU_Bernstein = [0.0384, 0.1100, 0.3368, 1.187]
CPU_Lagrange  = [0.0807, 0.3820, 2.5233, 26.52]

pylab.plot(log2(Ns), log2(CPU_Taylor))
pylab.plot(log2(Ns), log2(CPU_sine))
pylab.plot(log2(Ns), log2(CPU_Bernstein))
pylab.plot(log2(Ns), log2(CPU_Lagrange))
pylab.legend(["Taylor", "sine", "Bernstein", "Lagrange"])
pylab.show()




 

