import numpy as np

random_array = np.random.normal(0, 1, (10, 4)) # Стандартное нормальное распределение с
                                                              # математическим ожиданием μ = 0 и стандартным отклонением σ = 1

first_five_rows = random_array[:5]

print("Сгенерированный массив:")
print(random_array)

print("Минимальное значение:", np.min(random_array))
print("Максимальное значение:", np.max(random_array))
print("Среднее значение:", np.mean(random_array))
print("Стандартное отклонение:", np.std(random_array))

print("Первые 5 строк массива:")
print(first_five_rows)