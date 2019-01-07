'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import numpy as np


def f(x, y):
    return np.float(mapZ[float(x),float(y)])

f2 = np.vectorize(f)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#data = open("exp001.dat",'r')
data = open("exp-2lp.dat",'r')

dataV = []
for line in data:
	dataV.append(line)

mapZ = {}

x = []
y = []
z1 = []
z2 = []


for i in range(2,len(dataV)):
	
	#if float(dataV[i].split()[3]) >= 0:
		x.append(float(dataV[i].split()[0]))
		y.append(float(dataV[i].split()[1]))
		z1.append(float(dataV[i].split()[2]))
		#z2.append(float(dataV[i].split()[3]))
		# mapZ[float(x[i-2]),float(y[i-2])] = z1[i-2]
	
#print(mapZ)
# X = np.array(x)
# Y = np.array(y)

X, Y = np.meshgrid(x, y)

#Z = f(X,Y)


# ax = plt.axes(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')

# plt.show()

# xi = np.linspace(min(x), max(x))
# yi = np.linspace(min(y), max(y))

# X, Y = np.meshgrid(xi, yi)
# Z = griddata(x, y, z1, xi, yi)



#surf = ax.plot_surface(X, Y, f2(X,Y), rstride=5, cstride=5, cmap=cm.jet,
#                        linewidth=1, antialiased=True)

# ax.set_zlim3d(np.min(Z), np.max(Z))
# fig.colorbar(surf)

# plt.show()

#ax.plot3D(x, y, z1, 'gray')
ax.scatter3D(x, y, z1, c=z1, cmap='seismic')
#ax.scatter3D(x, y, z2, c=z2, cmap='seismic')

plt.show()