import numpy as np
import matplotlib.pyplot as plt
def lisajous(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

# Параметры для графиков
frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]
delta = np.pi / 2

# Создаем фигуры
plt.figure(figsize=(12, 10))

for i, (a, b) in enumerate(frequencies):
    t = np.linspace(0, 2 * np.pi, 1000)  # Временной интервал
    x, y = lisajous(a, b, delta, t)      # Получаем координаты

    plt.subplot(2, 2, i + 1)              # Создаем подграфик
    plt.plot(x, y)
    plt.title(f'Фигура Лисажу: a={a}, b={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')                     # Одинаковый масштаб по осям
    plt.grid()

plt.tight_layout()
plt.show()