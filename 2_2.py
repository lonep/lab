import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-5, 5, 50) 

fig, ax = plt.subplots()  
ax.plot(x, np.sin(x), label='sin(X)')
ax.plot(x, x - x**3/6 + x**5/120 - x**7/5040, label='f(X)')
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_title("EX 2_2")
ax.legend()
plt.show()
