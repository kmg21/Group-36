import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the angular momentum sphere
u = np.linspace(0, 2*np.pi, 10000)
v = np.linspace(0, np.pi, 10000)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

# plot the angular momentum sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha = 0.3)

# define the function of intersection points of ellipsoid and the sphere
def intersections(K, M, I):
    """
    Define the function for finding the intersection points of 
    the angular momentum sphere and the kinetic energy ellipsoid. (In R3)
    Method is convert the coordinate into spherical coordinate and use two functions get intersection points.

    Args:
        K (integer): the radius of angular momentum sphere
        M (integer): the constant of Hamiltonian, rotational kinetic energy
        I (list): length 3 list, which represents the moment of inertia

    The function will return 3 numpy arrays, which represent the corresponding coordinates (x, y, z) of intersection points.
    Note: 
        This will only give the intersection points on uppersphere.
    """

    phi = np.linspace(0, np.pi, 10000) # define phi
    a, b, c = I[0], I[1], I[2]

    costheta2 = (K - (2*a*M - 2*b*M)*(np.cos(phi))**2 - 2*b*M)/(2*c*M - (2*a*M - 2*b*M)*(np.cos(phi))**2 - 2*b*M)
    theta = np.arccos(np.sqrt(costheta2))
    interx = np.sqrt(2*a*M)*np.cos(phi)*np.sin(theta)
    intery = np.sqrt(2*b*M)*np.sin(phi)*np.sin(theta)
    interz = np.sqrt(2*c*M)*np.cos(theta)

    return interx, intery, interz

# define the moment of inertia in three directions (here we take 1, 2, 3 as example)
I = [0.25, 0.64, 4]

# define different constant for Hamiltonian and draw them
T = np.linspace(0.125, 1/1.28, 3)
T = np.append(T, np.linspace(1/1.28, 2, 5))

for M in T:
    interx, intery, interz = intersections(1, M, I)
    ax.plot3D(interx, intery, interz, color='black')
    ax.plot3D(interx, intery, -interz, color='black')
    ax.plot3D(interx, -intery, interz, color='black')
    ax.plot3D(interx, -intery, -interz, color='black')

interx, intery, interz = intersections(1, 0.64, I)
ax.plot3D(interx, intery, interz, color='black')
ax.plot3D(interx, intery, -interz, color='black')
ax.plot3D(interx, -intery, interz, color='black')
ax.plot3D(interx, -intery, -interz, color='black')

plt.show()
