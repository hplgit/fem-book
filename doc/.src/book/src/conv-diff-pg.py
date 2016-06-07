from sympy import * 
import numpy, pylab 

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
  else: print "series type unknown " # sys.exit(0)


N = 15 
#series_type = "Bernstein"
#series_type = "sin"
series_type = "Bernstein"
Omega = [0, 1]
x = Symbol("x")

psi = series(series_type, N)

eps = 0.3 
f = 1 
beta = 1.0


eps_vals =[1.0, 0.1, 0.01, 0.001]
for eps in eps_vals: 
  A = zeros((N-1), (N-1))
  b = zeros((N-1))

  psi = series(series_type, N)
  for i in range(0, N-1):  
    psi[i] = psi[i] + beta*diff(psi[i]) 
    integrand = f*psi[i]
    print integrand
    b[i,0] = integrate(integrand, (x, Omega[0], Omega[1])) 
    for j in range(0, N-1): 
      integrand = eps*diff(psi[i], x)* diff(psi[j], x) -  diff(psi[i], x)*psi[j] 
      A[i,j] = integrate(integrand, (x,Omega[0], Omega[1])) 
   
# bc 
#A[0,:] = zeros((1,N+1)) 
#A[0,0] = 1 
#b[0] = 1 

#A[N,:] = zeros((1,N+1)) 
#A[N,N] = 1 
#b[N] = 0 


#print A

  c = A.LUsolve(b)
  print c 
  u = sum(c[r,0]*psi[r] for r in range(N-1)) + x



  U = lambdify([x], u)
  xx = numpy.arange(Omega[0], Omega[1], 1/((N+1)*100.0)) 
  UU = U(xx)
  pylab.plot(xx, UU)
  print UU[-1], UU[-2]

pylab.legend(["eps=%e" %eps for eps in eps_vals], loc="lower right")
pylab.show()



