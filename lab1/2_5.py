import numpy as np
import matplotlib.pyplot as plt

def cos_(x):
    h = 1e-5
    return (np.cos(x+h)-np.cos(x))/h

left  = float(input("Left limit: "))
right = float(input("Right limit: "))

x = np.linspace(left, right, 50)

fig, ax = plt.subplots()
ax.plot(x, cos_(x), label="methodically")
ax.plot(x, np.cos(x), label="actually")

ax.legend()
plt.show()
