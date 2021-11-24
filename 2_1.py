import numpy as np
def func(x,w,b):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]*w[i]
    return sum + b

x = np.fromstring(input("x = "), dtype=int, sep=' ')
w = np.fromstring(input("w = "), dtype=int, sep=' ')
b = float(input("b = "))

print("Result: ", func(x,w,b))

