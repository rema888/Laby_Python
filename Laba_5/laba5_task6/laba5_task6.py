import sys
from pathlib import Path

# Проверяем, переданы ли аргументы командной строки
if len(sys.argv) == 1:
    print('No args')
else:
    p_name = sys.argv[1]  # Первый аргумент (имя параметра)
    dirpath = Path(sys.argv[2])  # Второй аргумент (путь к директории)

    # Проверяем, является ли первый аргумент '--dirpath'
    if p_name == '--dirpath':
        # Открываем файл для чтения
        with open('C:/Users/Nitro5/PycharmProjects/pythonProject/laba_5/laba5_task5/laba5_task5_nonexist.out') as file:
            # Читаем строки из файла и убираем лишние пробелы
            files = [row.strip() for row in file]

        print(files)  # Выводим список файлов, которые нужно создать

        # Проходим по каждому имени файла в списке
        for i in range(len(files)):
            # Создаем пустой файл в указанной директории
            with open(Path(dirpath / files[i]), 'a'):
                pass  #pass используется, чтобы ничего не делать, просто создаем файл
    else:
        print('Unknown args')

# Введя в терминал: python C:\Users\Nitro5\PycharmProjects\pythonProject\laba_5\laba5_task6\laba5_task6.py
#                   --dirpath C:\Users\Nitro5\PycharmProjects\pythonProject\laba_5\laba5_task6
#                   --files file1.txt file2.txt file3.txt
# получил: ['file2.txt', 'file3.txt']

# Таким образом, файлы file2.txt и file3.txt создались в папке laba5_task6