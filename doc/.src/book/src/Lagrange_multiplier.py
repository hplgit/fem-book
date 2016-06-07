
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xs = arange(-2, 2, 0.3)
ys = arange(-2, 2, 0.3)
X, Y = meshgrid(xs, ys)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

f = zeros([len(xs), len(ys)])
for i in range(0, len(xs)): 
  x = xs[i]
  for j in range(0, len(ys)): 
    y = ys[j]
    f[i,j] = x**2 + y**2 


g = zeros([len(xs)])
y = zeros([len(xs)])
for i in range(0, len(xs)): 
  x = xs[i]
  for j in range(0, len(ys)): 
    y[i] = 2 - x   
    g = 1 



ax.plot_wireframe(X, Y, f)
ax.plot(xs, y, g, color="r")
plt.show()




