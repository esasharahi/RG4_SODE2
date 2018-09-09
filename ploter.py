## esasharahi@gmail.com
#!/usr/bin/python
import numpy as np  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig2d = plt.figure()
fig3d = plt.figure()

data1 = np.loadtxt('points1.txt')
data2 = np.loadtxt('points2.txt')

data3 = np.loadtxt('points3d.txt')

ax = fig2d.add_subplot(1, 1, 1)
ax.plot(data1[:,0], data1[:,1], c = 'red', label = '$y_1$')
ax.plot(data2[:,0], data2[:,1], c = 'blue', label = '$y_2$')
leg = ax.legend()
ax.set_title("Runge-Kutta4 Method for the $\mathrm{d}y_i / \mathrm{d}t = f_i(t, y_1, y_2)$")
ax.set_xlabel('$t$')
ax.set_ylabel('$y_i$')

ax3d = plt.axes(projection='3d')
ax3d.plot(data3[:,0], data3[:,1], data3[:,2], c = 'violet', label = '$(t, y_1, y_2)$')
leg = ax3d.legend(bbox_to_anchor=(0.1, 0))
ax3d.set_title("Curve derived from the Runge-Kutta4 Method for the $\mathrm{d}y_i / \mathrm{d}t = f_i(t, y_1, y_2)$")
ax3d.set_xlabel('$t$')
ax3d.set_ylabel('$y_1$')
ax3d.set_zlabel('$y_2$')

fig2d.savefig('Runge-Kutta_Result.eps', format='eps', dpi=1000)
fig3d.savefig('Runge-Kutta_Result_3d.eps', format='eps', dpi=1000)
plt.show()
