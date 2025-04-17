import numpy as np

a = np.arange(16).reshape(4,4)
print("Исходный массив:\n", a)

a[[0, 2]] = a[[2, 0]]

print("После обмена строк 1 и 3:\n", a)