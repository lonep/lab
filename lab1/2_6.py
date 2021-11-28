import numpy as np

def twoVecAngle(vector1, vector2):
    v0 = vector1 / np.linalg.norm(vector1)
    v1 = vector2 / np.linalg.norm(vector2)
    result = np.degrees(np.arccos(np.dot(v0,v1))) 
    return result

Size = int(input("Set multitude size:"))

VectorSize = int(input("Set vectors size: "))

vectors = np.empty((Size, VectorSize),dtype=float)



vectors = np.empty((Size, VectorSize),dtype=float)
vectors = np.random.uniform(low=-100, high=100, size=(Size, VectorSize))
vector  = np.random.uniform(low=-100, high=100, size=VectorSize)


low90 = 0
low30 = 0
for i in range(Size):
    if ( twoVecAngle(vectors[i],vector) < 90):
        low90 += 1
    if (twoVecAngle(vectors[i],vector) < 30):
        low30 += 1
        
print("< 90: ", low90 / Size)
print("< 30: ", low30 / Size)
