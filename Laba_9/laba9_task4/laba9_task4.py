import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

index = np.where(x[:-1] == 0)[0] + 1  # +1 для получения индексов элементов после нуля

# Извлекаем элементы по найденным индексам
elements_after_zero = x[index]

max_element = np.max(elements_after_zero)

print("Исходный массив:", x)
print("Максимальный элемент среди элементов, перед которыми стоит ноль:", max_element)