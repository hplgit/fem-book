import sympy as sym
# Mesh: |--------|-------|
#       0      pi/2      pi
#
# Basis functions:
#
#   phi_0   phi_1   phi_2
#     \      /\      /
#      \    /  \    /
#       \  /    \  /
#        \/      \/
#     |-------|-------|
#     0      pi/2     pi

x = sym.Symbol('x')
A = sym.zeros(3,3)
f = sym.sin

phi_0 = 1 - (2*x)/sym.pi
phi_1l = 2*x/sym.pi          # left part of phi_1
phi_1r = 2 - (2*x)/sym.pi    # right part of phi_1
phi_2 = x/(sym.pi/2) - 1
node_0 = 0
node_1 = sym.pi/2
node_2 = sym.pi

# Diagonal terms
A[0,0] = sym.integrate(phi_0**2,  (x, node_0, node_1))
A[1,1] = sym.integrate(phi_1l**2, (x, node_0, node_1)) + \
         sym.integrate(phi_1r**2, (x, node_1, node_2))
A[2,2] = sym.integrate(phi_2**2,  (x, node_1, node_2))

# Off-diagonal terms
A[0,1] = sym.integrate(phi_0*phi_1l, (x, node_0, node_1))
A[1,0] = A[0,1]

A[1,2] = sym.integrate(phi_1r*phi_2, (x, node_1, node_2))
A[2,1] = A[1,2]

print('A:\n', A)  # Can compare with general matrix, h=pi/2

b = sym.zeros(3,1)

b[0] = sym.integrate(phi_0*f(x),  (x, node_0, node_1))
b[1] = sym.integrate(phi_1l*f(x), (x, node_0, node_1)) + \
       sym.integrate(phi_1r*f(x), (x, node_1, node_2))
b[2] = sym.integrate(phi_2*f(x),  (x, node_1, node_2))

print('b:\n', b)

c = A.LUsolve(b)
print('c:\n', c)

for i in range(len(c)):
    print('c[%d]=%g' % (i, c[i].evalf()))
print('u(pi/2)=%g' % c[1])

# For reports
print(sym.latex(A))
print(sym.latex(b))
print(sym.latex(c))
