
from math import * 

from sys import argv 
if len(argv) != 6: 
  print "usage: > Newton_demo.py f dfx x0 xmin xmax " 

f_str = argv[1]
dfdx_str = argv[2]
x0 = float(argv[3])
xmin = float(argv[4])
xmax = float(argv[5])



i = 0
tol = 1.0e-9 
maxit = 100 
f = 1 
x = x0
while abs(f) > tol and i <= maxit and x > xmin and x < xmax :  
  f = eval(f_str, vars())
  dfdx = eval(dfdx_str, vars())
  x = x0 - f/dfdx

  x0 = x 
  print "x=%.3e   f=%.3e   dfdx=%.3e " %  (x, f, dfdx)  
  i = i+1 

