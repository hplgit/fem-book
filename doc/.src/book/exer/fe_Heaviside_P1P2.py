import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src'))
from fe_approx1D_numint import mesh_uniform, u_glob
from fe_approx1D import basis
import numpy as np

def element_matrix(phi, Omega_e, numint):
    n = len(phi)
    A_e = np.zeros((n, n))
    h = Omega_e[1] - Omega_e[0]
    detJ = h/2  # dx/dX
    for r in range(n):
        for s in range(r, n):
            for j in range(len(numint[0])):
                Xj, wj = numint[0][j], numint[1][j]
                A_e[r,s] += phi[r](Xj)*phi[s](Xj)*detJ*wj
            A_e[s,r] = A_e[r,s]
    return A_e

def element_vector(f, phi, Omega_e, numint):
    n = len(phi)
    b_e = np.zeros(n)
    h = Omega_e[1] - Omega_e[0]
    detJ = h/2
    for r in range(n):
        for j in range(len(numint[0])):
            Xj, wj = numint[0][j], numint[1][j]
            xj = (Omega_e[0] + Omega_e[1])/2 + h/2*Xj  # mapping
            b_e[r] += f(xj)*phi[r](Xj)*detJ*wj
    return b_e


def assemble(vertices, cells, dof_map, phi, f, numint):
    N_n = len(list(set(np.array(dof_map).ravel())))
    N_e = len(cells)
    A = np.zeros((N_n, N_n))
    b = np.zeros(N_n)
    for e in range(N_e):
        Omega_e = [vertices[cells[e][0]], vertices[cells[e][1]]]
        A_e = element_matrix(phi[e], Omega_e, numint)
        b_e = element_vector(f, phi[e], Omega_e, numint)
        #print('element', e)
        #print(b_e)
        for r in range(len(dof_map[e])):
            for s in range(len(dof_map[e])):
                A[dof_map[e][r],dof_map[e][s]] += A_e[r,s]
            b[dof_map[e][r]] += b_e[r]
    return A, b

def approximate(f, d, N_e, numint, Omega=[0,1], filename='tmp'):
    """
    Compute the finite element approximation, using Lagrange
    elements of degree d, to a Python functionn f on a domain
    Omega. N_e is the number of elements.
    numint is the name of the numerical integration rule
    (Trapezoidal, Simpson, GaussLegendre2, GaussLegendre3,
    GaussLegendre4, etc.). numint=None implies exact
    integration.
    """
    from math import sqrt
    numint_name = numint  # save name
    if numint == 'Trapezoidal':
        numint = [[-1, 1], [1, 1]]
    elif numint == 'Simpson':
        numint = [[-1, 0, 1], [1./3, 4./3, 1./3]]
    elif numint == 'Midpoint':
        numint = [[0], [2]]
    elif numint == 'GaussLegendre2':
        numint = [[-1/sqrt(3), 1/sqrt(3)], [1, 1]]
    elif numint == 'GaussLegendre3':
        numint = [[-sqrt(3./5), 0, sqrt(3./5)],
                  [5./9, 8./9, 5./9]]
    elif numint == 'GaussLegendre4':
        numint = [[-0.86113631, -0.33998104,  0.33998104,
                   0.86113631],
                  [ 0.34785485,  0.65214515,  0.65214515,
                    0.34785485]]
    elif numint == 'GaussLegendre5':
        numint = [[-0.90617985, -0.53846931, -0.        ,
                   0.53846931,  0.90617985],
                  [ 0.23692689,  0.47862867,  0.56888889,
                    0.47862867,  0.23692689]]
    elif numint is not None:
        print('Numerical rule %s is not supported '\
              'for numerical computing' % numint)
        sys.exit(1)


    vertices, cells, dof_map = mesh_uniform(N_e, d, Omega)

    # phi is a list where phi[e] holds the basis in cell no e
    # (this is required by assemble, which can work with
    # meshes with different types of elements).
    # len(dof_map[e]) is the number of nodes in cell e,
    # and the degree of the polynomial is len(dof_map[e])-1
    phi = [basis(len(dof_map[e])-1) for e in range(N_e)]

    A, b = assemble(vertices, cells, dof_map, phi, f,
                    numint=numint)

    print('cells:', cells)
    print('vertices:', vertices)
    print('dof_map:', dof_map)
    print('A:\n', A)
    print('b:\n', b)
    c = np.linalg.solve(A, b)
    print('c:\n', c)

    if filename is not None:
        title = 'P%d, N_e=%d' % (d, N_e)
        title += ', integration: %s' % numint_name
        x_u, u, _ = u_glob(np.asarray(c), vertices, cells, dof_map,
                           resolution_per_element=51)
        x_f = np.linspace(Omega[0], Omega[1], 10001) # mesh for f
        import scitools.std as plt
        plt.plot(x_u, u, '-',
                 x_f, f(x_f), '--')
        plt.legend(['u', 'f'])
        plt.title(title)
        plt.savefig(filename + '.pdf')
        plt.savefig(filename + '.png')
    return c

def exercise():
    def f(x):
        if isinstance(x, (float,int)):
            return 0 if x < 0.5 else 1
        elif isinstance(x, np.ndarray):
            return np.where(x < 0.5, 0, 1)

    N_e_values = [2, 4, 8, 16]
    for d in 1, 2, 3, 4:
        for N_e in N_e_values:
            approximate(f, numint='GaussLegendre%d' % (d+1),
                        d=d, N_e=N_e,
                        filename='fe_Heaviside_P%d_%de' % (d, N_e))
        for ext in 'pdf', 'png':
            cmd = 'doconce combine_images '
            cmd += ext + ' -2 '
            cmd += ' '.join(['fe_Heaviside_P%d_%de' % (d, N_e)
                             for N_e in N_e_values])
            cmd += ' fe_Heaviside_P%d' % d
            print(cmd)
            os.system(cmd)

if __name__ == '__main__':
    exercise()
