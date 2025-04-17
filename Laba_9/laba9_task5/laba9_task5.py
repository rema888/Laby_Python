import numpy as np
from scipy.stats import multivariate_normal
from numpy.linalg import det, inv
import time

def log_multivariate_normal_pdf(X, m, C): # X - точки, размер (N, D); m - мат. ожидание, вектор длины D;
                                          # C - ковариационная матрица, размер (D, D)

    # Преобразуем входные данные в массивы NumPy
    X = np.asarray(X)
    m = np.asarray(m)
    C = np.asarray(C)

    D = m.shape[0] # Возвращает размерность пространства
    diff = X - m  # Матрица разностей размера (N, D)

    # Вычисление квадратичной формы для каждой точки x в X
    quadratic = np.einsum('ni,ij,nj->n', diff, inv(C), diff)

    # Формула логарифма плотности многомерного нормального распределения
    log_pdf = -0.5 * (D * np.log(2 * np.pi) + np.log(det(C)) + quadratic)
    return log_pdf

def compare_with_scipy(N=1000, D=10, num_repeats=1000): # N - количество точек; D - размерность пространства;
                                                        # num_repeats - количество повторений для точного замера времени

    # Генерируем случайные данные
    np.random.seed(0)
    X = np.random.randn(N, D)  # Генерируем N точек в D-мерном пространстве
    m = np.random.randn(D)  # Вектор средних значений
    C = np.random.randn(D, D)  # Генерируем случайную матрицу
    C = C @ C.T  # Делаем матрицу положительно определенной (ковариационная матрица)

    print("\nСгенерированные данные:")
    print(f"Матрица X (первые 5 строк из {N}):")
    print(X[:5])
    print(f"\nВектор средних m:", m)
    print(f"\nКовариационная матрица C (первые 5x5 элементов для D = {D}):")
    print(C[:5,:5] if D >= 5 else C)  # Выводим часть матрицы для больших размерностей

    # Наша реализация - замер времени
    start = time.perf_counter()  # Точный таймер
    for _ in range(num_repeats):
        our_logpdf = log_multivariate_normal_pdf(X, m, C)  # Многократный вызов
    our_time = (time.perf_counter() - start) / num_repeats  # Среднее время

    # Тестирование SciPy реализации
    scipy_dist = multivariate_normal(m, C, allow_singular=False)  # Создаем распределение
    start = time.perf_counter()
    for _ in range(num_repeats):
        scipy_logpdf = scipy_dist.logpdf(X)  # Многократный вызов
    scipy_time = (time.perf_counter() - start) / num_repeats  # Среднее время

    # Сравнение точности
    abs_diff = np.abs(our_logpdf - scipy_logpdf)  # Поэлементная разница
    max_abs_diff = np.max(abs_diff)  # Максимальное расхождение
    mean_abs_diff = np.mean(abs_diff)  # Среднее расхождение

    print(f"Размерность: N = {N}, D = {D}")
    print(f"Количество повторов: {num_repeats}")
    print(f"Наша реализация (среднее время): {our_time:.9f} секунд")
    print(f"Scipy реализация (среднее время): {scipy_time:.9f} секунд")
    print(f"Максимальная абсолютная разница: {max_abs_diff:.6e}")
    print(f"Средняя абсолютная разница: {mean_abs_diff:.6e}")

compare_with_scipy()