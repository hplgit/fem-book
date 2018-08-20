#!/bin/bash

set -ex

python approx2D_ls_orth.py
python approx3D.py

python cable_1P2.py
#python cable_discont_load.py  # fails
python cable_sin.py
python cable_xn.py

python exp_powers.py

#python fe_Heaviside_P1P2.py  # fails
python fe_sin_P1.py
python fe_sparsity_pattern.py
#python fe_tanh_P1P2.py  # fails
#python fe_tanh_P3P4.py  # fails

python Fourier_ls.py

python fu_fem_int.py x  # arguments?

python logistic_p.py

python parabola_sin.py

#python Pd_approx_error.py  # fails

python product_arith_mean_sympy.py

python sin_powers.py

python tanh_Lagrange.py
python tanh_Lagrange_regression.py
python tanh_sines_approx_altsol.py
python tanh_sines_boundary_term.py
python tanh_sines.py

python u_xx_f_sympy_class.py
#python u_xx_xm_P1to4.py  # fails
