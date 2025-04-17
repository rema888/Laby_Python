import numpy as np

a = np.array([0,1,2,0,0,4,0,6,9])
indices = np.where(a != 0)[0]

print("Исходный массив:", a)
print("Индексы ненулевых элементов:", indices)