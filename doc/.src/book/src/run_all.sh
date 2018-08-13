#!/bin/bash

set -ex

python approx_fenics_2Dcase.py
python approx_fenics.py

python Bernstein_vs_Lagrange_plot.py
#python Bernstein_vs_Lagrange.py  # takes too long time

python borehole_fenics.py

#python conv-diff-pg.py  # fails
python conv_diff.py
#python conv-diff.py  # fails
#python conv-diff-stab.py  # fails

python convergence_rate_fem.py  # fails?
python convergence_rate_global.py
python convergence_rate_local.py

#python darcy1D_mixed.py  # fails
#python darcy1D.py  # fails

python diffop_lib.py

python dispersion_relations.py

python ex_approx1D.py run_parabola_by_linear_leastsq
python ex_approx1D.py run_parabola_by_taylor_leastsq_illconditioning
python ex_approx1D.py run_parabola_by_sines_leastsq
python ex_approx1D.py run_sin_by_powers 2
python ex_approx1D.py run_Lagrange_poly 2
python ex_approx1D.py run_sin_by_Lagrange_leastsq 2
python ex_approx1D.py run_abs_by_Lagrange_leastsq 2
python ex_approx1D.py run_parabola_by_linear_interp1
python ex_approx1D.py run_parabola_by_linear_interp2
python ex_approx1D.py run_parabola_by_quadratic_interp
python ex_approx1D.py run_sin_by_poly_interp 2
python ex_approx1D.py run_parabola_by_linear_regression
python ex_approx1D.py run_noisy_parabola_by_quadratic_regression
python ex_approx1D.py run_sin_by_Lagrange_interp_ 2
python ex_approx1D.py run_poly_by_Lagrange_interp_ 2 2
python ex_approx1D.py run_abs_by_Lagrange_interp_ 2
python ex_approx1D.py run_abs_by_Lagrange_interp__Cheb 2
python ex_approx1D.py run_abs_by_Lagrange_interp__conv

python ex_approx1D_session.py

python ex_approx2D.py run_linear

#python ex_fe_approx1D.py approx_intro  # fails
#python ex_fe_approx1D.py approx_easy  # fails
#python ex_fe_approx1D.py approx_hard  # fails

#python ex_fe_approx1D_session.py  # fails

python ex_varform1D.py

python fe1D.py

python fe_approx1D_v1.py  # arguments?

python fe_approx2D.py  # plot is empty

python fe_fast_approx1D.py  # arguments?

python integrate_Heaviside.py

python Lagrange_multiplier.py

python logistic_gen.py
python logistic.py

#python mx_poisson.py  # fails

python neumann_fixpoint.py
python neumann_lagrangemultipler.py

#python python Newton_demo.py  # fails
#python Newton_demo_session.sh  # fails

#python nitsche.py  # fails

#python ODE_Picard_tricks.py  # fails

#python pipecooling_fem.py  # fails

python plot_fe_approx2D.py

python plot_global_bell.py

python plot_phi.py phi
python plot_phi.py pattern 3 3 random
python plot_phi.py pattern 3 3 uniform
python plot_phi.py u_sines
python plot_phi.py u_P1

python sympy_bvp_exact.py

python tanh_approx.py

python u_xx_2_CD.py
python u_xx_f_sympy.py

#python varform1D_session.py  # fails
