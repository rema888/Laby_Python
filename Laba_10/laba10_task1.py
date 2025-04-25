import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

plt.figure(figsize=(10, 6)) # Создаем фигуру и оси

x = np.linspace(-1, 1, 400) # Диапазон значений x

degrees = range(1, 8) # Степени полиномов Лежандра

# Построение графиков для каждой степени
for n in degrees:
    Pn = legendre(n)  # Получаем полином Лежандра степени n
    y = Pn(x)         # Вычисляем значения полинома
    plt.plot(x, y, label=f'n = {n}')

# Настройка графика
plt.title('Полиномы Лежандра') # Заголовок изображения
plt.xlabel('x') # Подписываем ось x
plt.ylabel('P_n(x)') # Подписываем ось y
plt.grid() # Отображение сетки

# Размещаем легенду с выносками
plt.legend( bbox_to_anchor=(1.3, 1), title='Степени полиномов')

# Отображаем график
plt.tight_layout()
plt.show()