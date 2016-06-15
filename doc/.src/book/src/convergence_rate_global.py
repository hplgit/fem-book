# check convergence rate of Fourier series and 
# global polynomials on either an exponential 
# function or a Gaussian bell.  
# Plot log-log and do regression / least square . 
# Discuss the problems with using regression / least square 


import sympy as sym
from approx1D import least_squares 
import scipy
import scipy.integrate

def Lagrange_series(N): 
  psi = []
#  h = Rational(1, N)
  h = 1.0/N
  points = [i*h for i in range(N+1)]
  for i in range(len(points)): 
    p = 1 
    for k in range(len(points)): 
      if k != i:
        p *= (x - points[k])/(points[i] - points[k])
    psi.append(p)
  return psi


def Bernstein_series(N): 
  # FIXME: check if a normalization constant is common in the definition 
  # advantage is that the basis is always positive 
  psi = []
  for k in range(0,N+1): 
    psi_k = x**k*(1-x)**(N-k)  
    psi.append(psi_k)
  return psi



def Sinusoidal_series(N): 
  psi = []
  for k in range(1,N): 
    psi_k = sym.sin(sym.pi*k*x)
    psi.append(psi_k)
  return psi

def Taylor_series(N): 
  psi = []
  for k in range(1,N): 
    psi_k = x**k 
    psi.append(psi_k)
  return psi

def series(series_type, N): 
  if   series_type== "Taylor"     : return Taylor_series(N)
  elif series_type== "Sinusoidal" : return Sinusoidal_series(N)
  elif series_type== "Bernstein"  : return Bernstein_series(N)
  elif series_type== "Lagrange"   : return Lagrange_series(N)
  else: print "series type unknown " # sys.exit(0)

def convergence_rate_analysis(series_type, func): 
  Ns =[2, 4, 8, 16]
  norms = []
  for N in Ns: 

    psi = series(series_type, N)
    u, c = least_squares(gauss_bell, psi, Omega, False) 

    error2 = sym.lambdify([x], (func - u)**2)
    L2_norm = scipy.integrate.quad(error2, Omega[0], Omega[1])  
    L2_norm = scipy.sqrt(L2_norm)
    norms.append(L2_norm[0])

  print "Ns ", Ns
  print "norms ", norms 
  return Ns, norms 


Omega = [0, 1]
x = sym.Symbol("x")
gauss_bell = sym.exp(-(x-0.5)**2) - sym.exp(-0.5**2)
step = sym.Piecewise( (1, 0.25 < x), (0, True)  )- sym.Piecewise( (1, 0.75 < x), (0, True)  )
func = gauss_bell 

import pylab
series_types = ["Taylor", "Sinusoidal", "Bernstein", "Lagrange"]
for series_type in series_types: 
  Ns, norms = convergence_rate_analysis(series_type, func)
  pylab.loglog(Ns, norms)
#  pylab.semilogy(Ns, norms)
#  pylab.plot(Ns, norms)

pylab.legend(series_types)
pylab.show()






