
from fenics import *
import matplotlib.pyplot as plt

class A(Expression): 
    def eval(self, value, x): 
        value[0] = 1
        if x[0] > 0.5: value[0] = 0.1 

p_bc = Expression("x[0]", degree=2)

Ns = [2, 8, 32]
for N in Ns: 
    mesh = UnitIntervalMesh(N)
    P1 = FiniteElement("CG", mesh.ufl_cell(), 1)
    P2 = FiniteElement("DG", mesh.ufl_cell(), 0)
    P1xP2 = P1 * P2
    W = FunctionSpace(mesh, P1xP2)
    u, p = TrialFunctions(W)
    v, q = TestFunctions(W)

    f = Constant(0)
    n = FacetNormal(mesh)
    a_coeff = A(degree=1)

    a = (1/a_coeff)*u*v*dx + u.dx(0)*q*dx - v.dx(0)*p*dx  
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
    P1 = FiniteElement("CG", mesh.ufl_cell(), 1)
    P2 = FiniteElement("DG", mesh.ufl_cell(), 0)
    TH = P1 * P2
    W = FunctionSpace(mesh, TH)
    u, p = TrialFunctions(W)
    v, q = TestFunctions(W)

    f = Constant(0)
    n = FacetNormal(mesh)
    a_coeff = A(degree=2)

    a = (1/a_coeff)*u*v*dx + u.dx(0)*q*dx - v.dx(0)*p*dx  
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


