import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 2 * np.pi, 1000)

# Начальные параметры для двух волн
amp1_init = 1.0
freq1_init = 1.0
amp2_init = 1.0
freq2_init = 1.0

# Функция для обновления графиков
def update(val):
    # Получаем значения из слайдеров
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val

    # Вычисляем волны
    wave1 = amp1 * np.sin(freq1 * x)
    wave2 = amp2 * np.sin(freq2 * x)

    # Обновляем графики
    line_wave1.set_ydata(wave1)
    line_wave2.set_ydata(wave2)
    line_sum.set_ydata(wave1 + wave2)

    # Обновляем график
    fig.canvas.draw_idle()


# Создаем фигуру и оси для графиков
fig, ax = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.15, right=0.85, hspace=0.4)

# График первой волны
line_wave1, = ax[0].plot(x, amp1_init * np.sin(freq1_init * x), label='Волна 1', color='blue')
ax[0].set_title('Первая волна')
ax[0].legend()
ax[0].grid()

# График второй волны
line_wave2, = ax[1].plot(x, amp2_init * np.sin(freq2_init * x), label='Волна 2', color='orange')
ax[1].set_title('Вторая волна')
ax[1].legend()
ax[1].grid()

# График суммы волн
line_sum, = ax[2].plot(x, (amp1_init + amp2_init) * np.sin(freq1_init * x), label='Сумма волн', color='green')
ax[2].set_title('Сумма волн')
ax[2].legend()
ax[2].grid()

# Создаем слайдеры для первой волны (амплитуда и частота)
ax_amp1 = plt.axes([0.15, 0.01, 0.65, 0.03])
slider_amp1 = Slider(ax_amp1, 'Амплитуда Волны 1', 0.0, 5.0, valinit=amp1_init)
ax_freq1 = plt.axes([0.15, 0.05, 0.65, 0.03])
slider_freq1 = Slider(ax_freq1, 'Частота Волны 1', 0.5, 10.0, valinit=freq1_init)

# Создаем слайдеры для второй волны
ax_amp2 = plt.axes([0.15, 0.09, 0.65, 0.03])
slider_amp2 = Slider(ax_amp2, 'Амплитуда Волны 2', 0.0, 5.0, valinit=amp2_init)
ax_freq2 = plt.axes([0.15, 0.13, 0.65, 0.03])
slider_freq2 = Slider(ax_freq2, 'Частота Волны 2', 0.5, 10.0, valinit=freq2_init)

# Привязываем функцию обновления к слайдерам
slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

plt.show()