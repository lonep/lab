import matplotlib.pyplot as plt
import numpy as np

def transformation_plot(x,matrix):
    xNext = np.empty((p, 2))
    for i in range(p):
        for j in range(2):
            xNext[i,j] = x[i, 0]*matrix[0, j] + x[i, 1]*matrix[1, j]
    return xNext

p = int(input("Number of points: "))
x = np.empty((p, 2))
matrix = np.empty((2,2))

print("X = : ")

for i in range(p):
    x[i] = np.fromstring(input(), dtype=float, sep=' ')

print("Matrix: ")

for i in range(2):
    matrix[i] = np.fromstring(input(), dtype=float, sep=' ')
    
xNext = transformation_plot(x,matrix)

fig, ax = plt.subplots()

cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0,5, p)]

ax.set_facecolor('xkcd:salmon')

for i, clr in enumerate(colors,start=0):
    ax.plot(x[i,0],x[i,1], 'go',color=clr, label='{i}'.format(i=i+1))
    ax.plot(xNext[i,0], xNext[i,1], 'go', color=clr, label='{i} new'.format(i = i + 1))

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.set_title("2_4")


plt.show()
