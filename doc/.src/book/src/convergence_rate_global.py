# check convergence rate of Fourier series and 
# global polynomials on either an exponential 
# function or a Gaussian bell.  
# Plot log-log and do regression / least square . 
# Discuss the problems with using regression / least square 


import sympy as sym
from approx1D import least_squares 
import scipy
import scipy.integrate


def sin_series(N): 
  psi = []
  for k in range(1,N): 
    psi_k = sym.sin(sym.pi*k*x)
    psi.append(psi_k)
  return psi

def taylor_series(N): 
  psi = []
  for k in range(1,N): 
    psi_k = x**k 
    psi.append(psi_k)
  return psi

def series(series_type, N): 
  if series_type=="Taylor" : return taylor_series(N)
  elif series_type=="sin"  : return sin_series(N)
  else: print "series type unknown " # sys.exit(0)

def convergence_rate_analysis(series_type, func): 
  Ns =[5, 10, 15, 20, 25]
#  Ns =[2, 4, 8, 16, 32, 64]
  norms = []
  for N in Ns: 

    psi = series(series_type, N)
    u, c = least_squares(gauss_bell, psi, Omega, False) 

    error2 = sym.lambdify([x], (func - u)**2)
    L2_norm = scipy.integrate.quad(error2, Omega[0], Omega[1])  
    L2_norm = scipy.sqrt(L2_norm)

    print "L2_norm ", L2_norm  
    norms.append(L2_norm[0])

  print "Ns ", Ns
  print "norms ", norms 
  return Ns, norms 


Omega = [0, 1]
x = sym.Symbol("x")
gauss_bell = sym.exp(-(x-0.5)**2) - sym.exp(-0.5**2)
step = sym.Piecewise( (1, 0.25 < x), (0, True)  )- sym.Piecewise( (1, 0.75 < x), (0, True)  )
func = step

import pylab
series_types = ["Taylor", "sin"]
for series_type in series_types: 
  Ns, norms = convergence_rate_analysis(series_type, func)
  pylab.loglog(Ns, norms)

pylab.legend(series_types)
pylab.show()






