import sys, os
sys.path.insert(0, os.path.join(os.pardir, 'src-approx'))
from fe_approx1D_numint import approximate
from sympy import tanh, Symbol
x = Symbol('x')

steepness = 20
arg = steepness*(x-0.5)
approximate(tanh(arg), symbolic=False, numint='GaussLegendre2',
            d=1, N_e=4, filename='fe_p1_tanh_4e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre2',
            d=1, N_e=8, filename='fe_p1_tanh_8e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre2',
            d=1, N_e=16, filename='fe_p1_tanh_16e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre3',
            d=2, N_e=2, filename='fe_p2_tanh_2e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre3',
            d=2, N_e=4, filename='fe_p2_tanh_4e')
approximate(tanh(arg), symbolic=False, numint='GaussLegendre3',
            d=2, N_e=8, filename='fe_p2_tanh_8e')

