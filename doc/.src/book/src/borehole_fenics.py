from fenics import *
import numpy as np

def make_mesh(Theta, a, b, nr, nt):
    mesh = RectangleMesh(Point(a, 0), Point(b, 1), nr, nt, 'crossed')

    # First make a denser mesh towards r=a
    x = mesh.coordinates()[:,0]
    y = mesh.coordinates()[:,1]
    s = 1.3

    def denser(x, y):
        return [a + (b-a)*((x-a)/(b-a))**s, y]

    x_bar, y_bar = denser(x, y)
    xy_bar_coor = np.array([x_bar, y_bar]).transpose()
    mesh.coordinates()[:] = xy_bar_coor

    # Map onto to a "piece of cake"

    def cylinder(r, s):
        return [r*np.cos(Theta*s), r*np.sin(Theta*s)]

    x_hat, y_hat = cylinder(x_bar, y_bar)
    xy_hat_coor = np.array([x_hat, y_hat]).transpose()
    mesh.coordinates()[:] = xy_hat_coor
    return mesh

def solver(alpha,    # Diffusion coefficient
           u_a,      # Inner pressure
           u_b,      # Outer pressure
           Theta,    # Arc size
           x_a,      # Inner boundary
           x_b,      # Outer boundary
           nr,       # Resolution r direction
           nt,       # Resolution azimuthal direction
           degree,   # Element polynomial degree
           filename, # Name of VTK file
           ):
    # It is tempting to use a as inner boundary, but we overwrite
    # that variable with the bilinear form later!
    mesh = make_mesh(Theta, x_a, x_b, nr, nt)
    V = FunctionSpace(mesh, 'P', degree)

    # Define Dirichlet boundary conditions
    from math import sqrt
    def inner(x, on_boundary):
        """Return True if x on r=a with tolerance."""
        r = on_boundary and \
            abs(sqrt(x[0]**2 + x[1]**2) - x_a) < 1E-12
        print 'XXXa', r
        return r

    def outer(x, on_boundary):
        """Return True if x on r=b with tolerance."""
        r = on_boundary and \
            abs(sqrt(x[0]**2 + x[1]**2) - x_b) < 1E-12
        print 'XXXb', r
        return r

    bc_inner = DirichletBC(V, u_a, inner)
    bc_outer = DirichletBC(V, u_b, outer)
    bcs = [bc_inner, bc_outer]

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    a = alpha*dot(grad(u), grad(v))*dx
    L = Constant(0)*v*dx  # L = 0*v*dx = 0 does not work...

    # Compute solution
    u = Function(V)
    solve(a == L, u, bcs)

    # Save solution to file in VTK format
    vtkfile = File(filename + '.pvd')
    vtkfile << u

    u.rename('u', 'u'); plot(u); plot(mesh)
    interactive()
    return u

def problem():
    solver(alpha=1, u_a=2, u_b=0, Theta=pi/4, x_a=1, x_b=2, nr=2, nt=2, degree=2, filename='tmp')

if __name__ == '__main__':
    problem()
