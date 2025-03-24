import os
import shutil
import sys

def find_small_files(directory):
    small_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.path.getsize(file_path) < 2048:  # 2KB
                small_files.append(file_path)
    return small_files

def main():
    # Получаем путь к папке из аргументов командной строки или используем текущую папку
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()  # Текущая папка

    # Находим файлы меньше 2К
    small_files = find_small_files(directory)

    if small_files:
        print("Найденные файлы меньше 2К:")
        for file in small_files:
            print(file)

        # Создаем папку small и копируем туда найденные файлы
        small_folder = os.path.join(directory, 'small')
        os.makedirs(small_folder, exist_ok=True)

        for file in small_files:
            shutil.copy(file, small_folder)
        print(f"Файлы скопированы в папку: {small_folder}")
    else:
        print("Файлы меньше 2К не найдены.")

if __name__ == "__main__":
    main()