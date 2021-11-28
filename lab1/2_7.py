import numpy as np
import matplotlib.pyplot as plt

total_points = 100
size = float(input("Set size:" ))
dots_array = np.random.uniform(low=-size, high=size, size=(total_points, 2))

norm = np.array([np.linalg.norm(dot) for dot in dots_array])

fig, ax = plt.subplots()
#ax.scatter(dots_array[1, 0], dots_array[0,1])

ax.scatter(dots_array[norm <= 1,0],dots_array[norm <= 1,1])
ax.scatter(dots_array[norm > 1,0],dots_array[norm > 1,1],color='orange')

square = np.array([[-size,-size], [-size,size], [size, size], [size,-size], [-size,-size]])
x = np.linspace(0, np.pi*2, total_points)
ax.plot(np.cos(x),np.sin(x))
inside = len(norm[norm <= 1])
ax.plot(square[:,0],square[:,1], color='orange')
plt.text(-size, size, "Total points " +str(total_points), fontsize = 10)
plt.text(0, size, "Points inside " +str(inside), fontsize = 10)
plt.text(size, size, "Fraction " +str(len(norm[norm<=1])/len(norm)), fontsize = 10)

ax.set_aspect('equal')
plt.show()
