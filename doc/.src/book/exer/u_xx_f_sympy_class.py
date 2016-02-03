import sympy as sym
x, L, C, D, c_0, c_1, = sym.symbols('x L C D c_0 c_1')

class TwoPtBoundaryValueProblem(object):
    """
    Solve -(a*u')' = f(x) with boundary conditions
    specified in subclasses (method get_bc).
    a and f must be sympy expressions of x.
    """
    def __init__(self, f, a=1, L=L, C=C, D=D):
        """Default values for L, C, D are symbols."""
        self.f = f
        self.a = a
        self.L = L
        self.C = C
        self.D = D

        # Integrate twice
        u_x = - sym.integrate(f, (x, 0, x)) + c_0
        u = sym.integrate(u_x/a, (x, 0, x)) + c_1
        # Set up 2 equations from the 2 boundary conditions and solve
        # with respect to the integration constants c_0, c_1
        eq = self.get_bc(u)
        eq = [sym.simplify(eq_) for eq_ in eq]
        print 'BC eq:', eq
        self.u = self.apply_bc(eq, u)

    def apply_bc(self, eq, u):
        # Solve BC eqs respect to the integration constants
        r = sym.solve(eq, [c_0, c_1])
        # Substitute the integration constants in the solution
        u = u.subs(c_0, r[c_0]).subs(c_1, r[c_1])
        u = sym.simplify(sym.expand(u))
        return u

    def get_solution(self, latex=False):
        return sym.latex(self.u, mode='plain') if latex else self.u

    def get_residuals(self):
        """Return the residuals in the equation and BCs."""
        R_eq = sym.diff(sym.diff(self.u, x)*self.a, x) + self.f
        R_0, R_L = self.get_bc(self.u)
        residuals = [sym.simplify(R) for R in R_eq, R_0, R_L]
        return residuals

    def get_bc(self, u):
        raise NotImplementedError(
            'class %s has not implemented get_bc' %
            self.__class__.__name__)


class Model1(TwoPtBoundaryValueProblem):
    """u(0)=0, u(L)=D."""
    def get_bc(self, u):
        return [u.subs(x, 0)-0,               # x=0 condition
                u.subs(x, self.L) - self.D]   # x=L condition

class Model2(TwoPtBoundaryValueProblem):
    """u'(0)=C, u(L)=D."""
    def get_bc(self, u):
        return [sym.diff(u,x).subs(x, 0) - self.C, # x=0 cond.
                u.subs(x, self.L) - self.D]        # x=L cond.

class Model3(TwoPtBoundaryValueProblem):
    """u(0)=C, u(L)=D."""
    def get_bc(self, u):
        return [u.subs(x, 0) - self.C,
                u.subs(x, self.L) - self.D]

class Model4(TwoPtBoundaryValueProblem):
    """u(0)=0, -u'(L)=C*(u-D)."""
    def get_bc(self, u):
        return [u.subs(x, 0) - 0,
                -sym.diff(u, x).subs(x, self.L) -
                self.C*(u.subs(x, self.L) - self.D)]

def test_TwoPtBoundaryValueProblem():
    f = 2
    model = Model1(f)
    print 'Model 1, u:', model.get_solution()
    for R in model.get_residuals():
        assert R == 0

    f = x
    model = Model2(f)
    print 'Model 2, u:', model.get_solution()
    for R in model.get_residuals():
        assert R == 0

    f = 0
    a = 1 + x**2
    model = Model3(f, a=a)
    print 'Model 3, u:', model.get_solution()
    for R in model.get_residuals():
        assert R == 0

def demo_Model4():
    f = 0
    model = Model4(f, a=sym.sqrt(1+x))
    print 'Model 4, u:', model.get_solution()

if __name__ == '__main__':
    test_TwoPtBoundaryValueProblem()
    demo_Model4()
