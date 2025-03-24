import sys
from pathlib import Path

def main():
    # Проверяем, были ли переданы аргументы командной строки
    if len(sys.argv) < 5:
        print('Usage: script.py --dirpath <directory> --files <file1> <file2> ...')
        return

    # Получаем параметры из аргументов
    p_name = sys.argv[1]
    dirpath = Path(sys.argv[2])
    t_name = sys.argv[3]

    # Проверяем, что переданы правильные именованные параметры
    if p_name != '--dirpath' or t_name != '--files':
        print('Unknown args')
        return

    # Получаем список файлов, которые нужно проверить
    files = sys.argv[4:]

    # Проверяем, существует ли указанная директория
    if not dirpath.is_dir():
        print(f"Directory '{dirpath}' does not exist.")
        return

    # Получаем список всех файлов в указанной директории
    files_in_dir = {f.name for f in dirpath.iterdir() if f.is_file()}
    print(f"Files in directory '{dirpath}': {files_in_dir}")

    exist = []
    nonexist = []

    # Проверяем наличие каждого файла в директории
    for file in files:
        if file in files_in_dir:
            exist.append(file)
        else:
            nonexist.append(file)

    # Выводим результаты на экран
    print("Существующие файлы:")
    for file in exist:
        print(file)

    print("\nНесуществующие файлы:")
    for file in nonexist:
        print(file)

    # Записываем существующие файлы в файл 'laba5_task5_exist.out'
    with open('laba5_task5_exist.out', 'w') as f:
        f.write("\n".join(exist))

    # Записываем несуществующие файлы в файл 'laba5_task5_nonexist.out'
    with open('laba5_task5_nonexist.out', 'w') as f:
        f.write("\n".join(nonexist))

if __name__ == "__main__":
    main()

# Введя в терминал: python C:\Users\Nitro5\PycharmProjects\pythonProject\laba_5\laba5_task5\laba5_task5.py
#                           --dirpath C:\Users\Nitro5\PycharmProjects\pythonProject\laba_5\laba5_task5
#                           --files file1.txt file2.txt file3.txt
# получил: Files in directory 'C:\Users\Nitro5\PycharmProjects\pythonProject\laba_5\laba5_task5': {'laba5_task5.py', 'file1.txt'}
#          Существующие файлы:
#          file1.txt
#
#          Несуществующие файлы:
#          file2.txt
#          file3.txt