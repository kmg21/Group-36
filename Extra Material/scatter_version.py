import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def generate_ellipsoid_points(num_points, k):
    x = []
    y = []
    z = []
    
    u = np.linspace(0, 2*np.pi, num_points)
    v = np.linspace(0, np.pi, num_points)

    for phi in u:
        for theta in v:
            x1 = np.sqrt(1/k) * np.sin(theta) * np.cos(phi)
            y1 = np.sqrt(0.6/k) * np.sin(theta) * np.sin(phi)
            z1 = np.sqrt(0.3/k) * np.cos(theta)

            x.append(x1)
            y.append(y1)
            z.append(z1)
    
    return x, y, z


def generate_sphere_points(num_points):
    x = []
    y = []
    z = []

    inc = np.pi * (3 - np.sqrt(5))  # Golden angle increment
    offset = 2 / num_points  # Offset for even point distribution
    
    for i in range(num_points):
        y1 = ((i * offset) - 1) + (offset / 2)
        radius = np.sqrt(1 - y1**2)
        theta = i * inc

        x.append(np.cos(theta) * radius)
        y.append(y1)
        z.append(np.sin(theta) * radius)

    return x, y, z

# Example usage
num_points_sphere = 3000
num_points = 300

x11, y11, z11 = generate_ellipsoid_points(num_points, k=0.3)
x12, y12, z12 = generate_ellipsoid_points(num_points, k=0.4)
x13, y13, z13 = generate_ellipsoid_points(num_points, k=0.5)
x14, y14, z14 = generate_ellipsoid_points(num_points, k=0.6)
x15, y15, z15 = generate_ellipsoid_points(num_points, k=0.7)
x16, y16, z16 = generate_ellipsoid_points(num_points, k=0.8)
x17, y17, z17 = generate_ellipsoid_points(num_points, k=0.9)
x18, y18, z18 = generate_ellipsoid_points(num_points, k=1.0)
x2, y2, z2 = generate_sphere_points(num_points_sphere)


def line(x1, y1, z1, x2, y2, z2):
    linex, liney, linez = [], [], []
    for i in range(len(x1)):
        for j in range(len(x2)):
            if abs(x1[i] - x2[j]) < 0.015:
                if abs(y1[i] - y2[j]) < 0.015:
                    if abs(z1[i] - z2[j]) < 0.015:
                        linex.append(x1[i])
                        liney.append(y1[i])
                        linez.append(z1[i])
    return linex, liney, linez

line1x, line1y, line1z = line(x11, y11, z11, x2, y2, z2)
line2x, line2y, line2z = line(x12, y12, z12, x2, y2, z2)
line3x, line3y, line3z = line(x13, y13, z13, x2, y2, z2)
line4x, line4y, line4z = line(x14, y14, z14, x2, y2, z2)
line5x, line5y, line5z = line(x15, y15, z15, x2, y2, z2)
line6x, line6y, line6z = line(x16, y16, z16, x2, y2, z2)
line7x, line7y, line7z = line(x17, y17, z17, x2, y2, z2)
line8x, line8y, line8z = line(x18, y18, z18, x2, y2, z2)


fig = plt.figure(9)
ax = fig.add_subplot(projection='3d')

#ax.scatter(x11, y11, z11, color='r', s=0.001)
#ax.scatter(x18, y18, z18, s=0.05)
#ax.scatter(x14, y14, z14, s=0.05)
#ax.scatter(x16, y16, z16, s=0.05)
ax.scatter(x2, y2, z2, color='b', s=0.01)
ax.scatter(line1x, line1y, line1z, s=0.1)
ax.scatter(line2x, line2y, line2z, s=0.1)
ax.scatter(line3x, line3y, line3z, s=0.1)
ax.scatter(line4x, line4y, line4z, s=0.1)
ax.scatter(line5x, line5y, line5z, s=0.1)
ax.scatter(line6x, line6y, line6z, s=0.1)
ax.scatter(line7x, line7y, line7z, s=0.1)
ax.scatter(line8x, line8y, line8z, s=0.1)

plt.show()