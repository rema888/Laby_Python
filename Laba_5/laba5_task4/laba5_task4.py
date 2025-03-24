import os
import shutil
import sys
def find_small_files(directory):
    small_files = []  # Список для хранения найденных маленьких файлов
    # Проходим по всем подкаталогам и файлам в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  # Полный путь к файлу
            # Проверяем, является ли это файлом и меньше ли он 2КБ
            if os.path.isfile(file_path) and os.path.getsize(file_path) < 2048:  # 2KB
                small_files.append(file_path)  # Добавляем файл в список
    return small_files  # Возвращаем список найденных файлов


def main():
    # Получаем путь к папке из аргументов командной строки или используем текущую папку
    if len(sys.argv) > 1:
        directory = sys.argv[1]  # Если аргумент передан, используем его как директорию
    else:
        directory = os.getcwd()  # Если аргумент не передан, используем текущую директорию

    # Находим файлы меньше 2К
    small_files = find_small_files(directory)

    if small_files:
        print("Найденные файлы меньше 2К:")
        for file in small_files:
            print(file)

        # Создаем папку 'small' и копируем туда найденные файлы
        small_folder = os.path.join(directory, 'small')  # Путь к новой папке
        os.makedirs(small_folder, exist_ok=True)  # Создаем папку, если она не существует

        for file in small_files:
            shutil.copy(file, small_folder)  # Копируем каждый найденный файл в новую папку
        print(f"Файлы скопированы в папку: {small_folder}")
    else:
        print("Файлы меньше 2К не найдены.")


if __name__ == "__main__":
    main()