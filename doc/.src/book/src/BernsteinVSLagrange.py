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
    psi_k = sin(pi*k*x)
    psi.append(psi_k)
  return psi

def taylor_series(N): 
  # FIXME: do not satisfy bc  
  print "Cannot with current BC implementation" 
  return 
  psi = []
  for k in range(1,N): 
    psi_k = x**k 
    psi.append(psi_k)
  return psi

def series(series_type, N): 
  if series_type=="Taylor" : return taylor_series(N) # cannot do with current implementation of bc
  elif series_type=="sin"  : return sin_series(N)
  elif series_type=="Bernstein"  : return bernstein_series(N)
  elif series_type=="Lagrange"  : return lagrange_series(N)
  else: print "series type unknown " # sys.exit(0)




N = 10 
x = sym.Symbol("x")
bpsi = series("Bernstein", N)
lpsi = series("Lagrange", N)

print len(lpsi)
print len(bpsi)

for i in range(len(bpsi)): 
  print bpsi[i]
  print lpsi[i]


