
from fenics import *
import matplotlib.pyplot as plt

class K(Expression): 
    def eval(self, value, x): 
	value[0] = 1
	if x[0] > 0.5: value[0] = 0.1 

p_bc = Expression("x[0]")

Ns = [2, 8, 32]
for N in Ns: 
    mesh = UnitIntervalMesh(N)
    V = FunctionSpace(mesh, "CG", 1)
    Q = FunctionSpace(mesh, "DG", 0)
    W = MixedFunctionSpace([V,Q])
    u, p = TrialFunctions(W)
    v, q = TestFunctions(W)

    f = Constant(0)
    n = FacetNormal(mesh)
    k = K()

    a = (1/k)*u*v*dx + u.dx(0)*q*dx - v.dx(0)*p*dx  
    L = f*q*dx - p_bc*v*n[0]*ds  

    up = Function(W)
    solve(a == L, up)

    u, p = up.split()

    import numpy 
    a = numpy.array([0.0])
    b = numpy.array([0.0])
    xs = numpy.arange(0.0, 1.0, 0.001)
    ps = numpy.arange(0.0, 1.0, 0.001)
    for i in range(0,len(xs)): 
	a[0] = xs[i]  
	p.eval(b, a)  
	ps[i] = b 

    plt.plot(xs, ps)


plt.legend(["N=%d"%N for N in Ns], loc="upper left")
plt.savefig('darcy_a1D_mx.png'); plt.savefig('darcy_a1D_mx.pdf'); 
plt.show()


for N in Ns: 
    mesh = UnitIntervalMesh(N)
    V = FunctionSpace(mesh, "CG", 1)
    Q = FunctionSpace(mesh, "DG", 0)
    W = MixedFunctionSpace([V,Q])
    u, p = TrialFunctions(W)
    v, q = TestFunctions(W)

    f = Constant(0)
    n = FacetNormal(mesh)
    k = K()

    a = (1/k)*u*v*dx + u.dx(0)*q*dx - v.dx(0)*p*dx  
    L = f*q*dx - p_bc*v*n[0]*ds  

    up = Function(W)
    solve(a == L, up)

    u, p = up.split()

    import numpy 
    a = numpy.array([0.0])
    b = numpy.array([0.0])
    xs = numpy.arange(0.0, 1.0, 0.001)
    us = numpy.arange(0.0, 1.0, 0.001)
    for i in range(0,len(xs)): 
	a[0] = xs[i]  
	u.eval(b, a)  
	us[i] = b 

    plt.ylim([-0.4,-0.1])
    plt.plot(xs, us)


plt.legend(["N=%d"%N for N in Ns], loc="upper left")
plt.savefig('darcy_adx1D_mx.png'); plt.savefig('darcy_adx1D_mx.pdf'); 
plt.show()


