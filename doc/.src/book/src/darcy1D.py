from fenics import *
import matplotlib.pyplot as plt

class K(Expression): 
    def eval(self, value, x): 
	value[0] = 1
	if x[0] >= 0.5: value[0] = 0.1

class DirichletBoundary(SubDomain):
    def inside(self, x, on_boundary):
	return on_boundary 



p_bc = f = Expression("x[0]")

Ns = [2, 8, 32]
for N in Ns: 
    mesh = UnitIntervalMesh(N)
    V = FunctionSpace(mesh, "CG", 1)
    Q = FunctionSpace(mesh, "DG", 0)
    u = TrialFunction(V)
    v = TestFunction(V)
    k = K()
    a = k*inner(grad(u), grad(v))*dx 
    f = Constant(0)
    L = f*v*dx 
    bc = DirichletBC(V, p_bc, DirichletBoundary())
    u = Function(V)
    solve(a == L, u, bc)

    plt.plot(V.dofmap().tabulate_all_coordinates(mesh), u.vector().array())
    plt.hold(True)
plt.legend(["N=%d"%N for N in Ns], loc="upper left")
plt.savefig('darcy_a1D.png'); plt.savefig('darcy_a1D.pdf')
plt.show()

for N in Ns: 
    mesh = UnitIntervalMesh(N)
    V = FunctionSpace(mesh, "CG", 1)
    u = TrialFunction(V)
    v = TestFunction(V)
    k = K()
    a = k*inner(grad(u), grad(v))*dx 
    f = Constant(0)
    L = f*v*dx 
    bc = DirichletBC(V, p_bc, DirichletBoundary())
    u = Function(V)
    solve(a == L, u, bc)
    kux = project(-k*u.dx(0), V)

    plt.ylim([-0.4,-0.1])
    plt.plot(V.dofmap().tabulate_all_coordinates(mesh), kux.vector().array())
    plt.hold(True)
    plt.legend(["N=%d"%N for N in Ns], loc="upper left")
plt.savefig('darcy_adx1D.png'); plt.savefig('darcy_adx1D.pdf'); 
plt.show()


