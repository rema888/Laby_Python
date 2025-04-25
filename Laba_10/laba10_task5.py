import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаем сетку значений для x и y
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)

# Определяем функцию MSE
Z = (X - Y) ** 2

# Создаем фигуру и оси для графиков
fig = plt.figure(figsize=(12, 6))

# Первый график с линейной осью Z
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax1.set_title('MSE (линейная ось Z)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

# Второй график с логарифмической осью Z
ax2 = fig.add_subplot(122, projection='3d')
Z_log = np.log1p(Z)
ax2.plot_surface(X, Y, Z_log, cmap='plasma', edgecolor='none')
ax2.set_title('MSE (логарифмическая ось Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(MSE)')

plt.tight_layout()
plt.show()