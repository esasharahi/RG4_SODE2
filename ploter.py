## esasharahi@gmail.com
#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


fig2d = plt.figure()
fig3d = plt.figure()


with open('points1.txt') as f_1:
	lines = f_1.readlines()
	x1 = [line.split()[0] for line in lines]
	y1 = [line.split()[1] for line in lines]

with open('points2.txt') as f_2:
	lines = f_2.readlines()
	x2 = [line.split()[0] for line in lines]
	y2 = [line.split()[1] for line in lines]

with open('points3d.txt') as f3d:
	lines = f3d.readlines()
	t = [float(line.split()[0]) for line in lines]
	x = [float(line.split()[1]) for line in lines]
	y = [float(line.split()[2]) for line in lines]


ax = fig2d.add_subplot(1, 1, 1)
ax.plot(x1, y1, c = 'red', label = '$y_1$')
ax.plot(x2, y2, c = 'blue', label = '$y_2$')
leg = ax.legend()
ax.set_title("Runge-Kutta4 Method for the $\mathrm{d}y_i / \mathrm{d}t = f_i(t, y_1, y_2)$")
ax.set_xlabel('$t$')
ax.set_ylabel('$y_i$')


ax3d = plt.axes(projection='3d')
ax3d.plot(t, x, y, c = 'violet', label = '$(t, y_1, y_2)$')
leg = ax3d.legend(bbox_to_anchor=(0.1, 0))
ax3d.set_title("Curve derived from the Runge-Kutta4 Method for the $\mathrm{d}y_i / \mathrm{d}t = f_i(t, y_1, y_2)$")
ax3d.set_xlabel('$t$')
ax3d.set_ylabel('$y_1$')
ax3d.set_zlabel('$y_2$')


fig2d.savefig('Runge-Kutta_Result.eps', format='eps', dpi=1000)
fig3d.savefig('Runge-Kutta_Result_3d.eps', format='eps', dpi=1000)
plt.show()
