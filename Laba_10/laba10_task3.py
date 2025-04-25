import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def lisajous(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

# Параметры анимации
frames = 100  # Количество кадров
t = np.linspace(0, 2 * np.pi, 1000)  # Временной интервал
delta = 0  # Нулевой сдвиг фаз

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], lw=2)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid()

# Инициализация функции для анимации
def init():
    line.set_data([], [])
    return line,

# Функция обновления для анимации
def update(frame):
    a = frame / frames * 10  # Изменяем частоту a от 0 до 10
    b = 1                     # Частота b фиксирована
    x, y = lisajous(a, b, delta, t)  # Получаем координаты
    line.set_data(x, y)      # Обновляем данные линии
    return line,

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=frames, init_func=init,
                    blit=True, interval=50)

plt.title('Анимация вращения фигуры Лисажу')
plt.show()