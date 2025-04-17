import numpy as np

matrix = np.loadtxt('file_for_laba9_task1.txt', delimiter =',') # читаем данные и возвращаем их в виде массива numpy

print("Сумма всех элементов:", np.sum(matrix))
print("Максимальный элемент:", np.max(matrix))
print("Минимальный элемент:", np.min(matrix))