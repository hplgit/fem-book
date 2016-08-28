import sympy as sym 
import numpy, pylab 

def lagrange_series(N): 
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
  psi = psi[1:-1]
  return psi


def bernstein_series(N): 
  # FIXME: check if a normalization constant is common in the definition 
  # advantage is that the basis is always positive 
  psi = []
#  for k in range(0,N+1): 
  for k in range(1,N):  # bc elsewhere  
    psi_k = x**k*(1-x)**(N-k)  
    psi.append(psi_k)
  return psi


def sin_series(N): 
  # FIXME: do not satisfy bc  
  psi = []
  for k in range(1,N): 
    psi_k = sym.sin(sym.pi*k*x)
    psi.append(psi_k)
  return psi


def series(series_type, N): 
  if series_type=="sin"  : return sin_series(N)
  elif series_type=="Bernstein"  : return bernstein_series(N)
  elif series_type=="Lagrange"  : return lagrange_series(N)
  else: print "series type unknown " # sys.exit(0)


def test_epsilon(N, series_type, Omega):
  psi = series(series_type, N)
  f = 1 
  eps_vals =[1.0, 0.1, 0.01, 0.001]
  for eps in eps_vals: 
    A = sym.zeros((N-1), (N-1))
    b = sym.zeros((N-1))

    for i in range(0, N-1):  
      integrand = f*psi[i]
      integrand = sym.lambdify([x], integrand)
      b[i,0] = sym.mpmath.quad(integrand, [Omega[0], Omega[1]]) 
      for j in range(0, N-1): 
	integrand = eps*sym.diff(psi[i], x)* sym.diff(psi[j], x) -  sym.diff(psi[i], x)*psi[j] 
	integrand = sym.lambdify([x], integrand)
	A[i,j] = sym.mpmath.quad(integrand, [Omega[0], Omega[1]]) 

    c = A.LUsolve(b)
    u = sum(c[r,0]*psi[r] for r in range(N-1)) + x

    U = sym.lambdify([x], u)
    xx = numpy.arange(Omega[0], Omega[1], 1/((N+1)*100.0)) 
    UU = U(xx)
    pylab.plot(xx, UU)

  pylab.legend(["eps=%e" %eps for eps in eps_vals], loc="upper left")
  pylab.show()



N = 8 
series_type = "Bernstein"
#series_type = "sin"
#series_type = "Lagrange"
Omega = [0, 1]
x = sym.Symbol("x")

test_epsilon(N, series_type, Omega)



