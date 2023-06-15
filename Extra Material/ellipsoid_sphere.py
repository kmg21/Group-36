import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the ellipsoid (here we use the sphere for easier calculation)
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha = 0.5)


# define the ellipsoid
x3 = 0.5 * np.outer(np.cos(u), np.sin(v))
y3 = 0.8 * np.outer(np.sin(u), np.sin(v))
z3 = 2 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x3, y3, z3, alpha = 0.1)
'''
n = len(u)
intersectx = []
intersecty = []
intersectz = []
for i in range(n):
    for j in range(n):
        if (x3[i, j])**2 + (y3[i, j])**2 + (z3[i, j])**2 == 1:
            intersectx.append(x[i][j])
            intersecty.append(y[i][j])
            intersectz.append(z[i][j])

interx = np.outer(np.ones(len(intersectx)), np.array(intersectx))
intery = np.outer(np.ones(len(intersecty)), np.array(intersecty))
interz = np.outer(np.ones(len(intersectz)), np.array(intersectz))
ax.plot3D(interx, intery, interz, color='black')
'''


phi = np.linspace(0, 2*np.pi, 100)
costheta2 = (0.36+0.39*np.cos(phi)*np.cos(phi))/(3.36+0.39*np.cos(phi)*np.cos(phi))
theta = np.arccos(np.sqrt(costheta2))
interx = 0.5*np.cos(phi)*np.sin(theta)
intery = 0.8*np.sin(phi)*np.sin(theta)
interz = 2*np.cos(theta)
ax.plot3D(interx, intery, interz, color='red')
ax.plot3D(interx, intery, -interz, color='red')

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
plt.show()