import os
import csv
import random
from collections import defaultdict

# Путь файла, с какой части таблицы выводим (сверху по умол.), сколько строк (5 по умол.), какой будет разделитель (',' по умол.)
def Show(file_path, output_type = 'top', num_rows = 5, separator = ','):

    with open(file_path) as f:
        headers = next(csv.reader(f))  # Считываем заголовки
        data = list(csv.reader(f))  # Считываем остальные строки

    if len(data) < num_rows:
        print(f"Недостаточно строк для вывода (в файле их {len(data)}, а должно быть минимум 5). Выводим все доступные строки:")
        rows_to_show = data

    else:
        if output_type == 'top':
            rows_to_show = data[:num_rows]
        elif output_type == 'bottom':
            rows_to_show = data[-num_rows:]
        elif output_type == 'random':
            rows_to_show = random.sample(data, min(num_rows, len(data)))
        else:
            print("Неверный тип вывода. Используйте 'top', 'bottom' или 'random'.")
            return

    print(separator.join(headers))  # Используем переданный разделитель
    print("-" * len(separator.join(headers)))  # Разделитель для визуального оформления

    for row in rows_to_show:
        print(separator.join(row))
    print()

# Show('ex_for_laba8.csv')
# Show('ex_for_laba8.csv', 'bbbbb', 2)
# Show('ex_for_laba8.csv', 'random', 6, '...')

# Если вызвать Show('ex_for_laba8.csv') и оставить в файле заголовок и 1 строку с данными, получим:
#      Недостаточно строк для вывода (в файле их 1, а должно быть минимум 5). Выводим все доступные строки:
#      userId,jobTitle,firstName,lastName,employeeCode,region,phoneNumber,emailAddress
#      -------------------------------------------------------------------------------
#      krish,Developer,Krish,Lee,E1,CA,123456,krish.lee@learningcontainer.com

def Info(file_path):
    with open(file_path) as f:
        headers = next(csv.reader(f))
        data = list(csv.reader(f))

    rows = len(data)
    cols = len(headers) if headers else 0 # Если нет строки заголовков
    print(f"Размер данных: {rows}x{cols}\n")

    print("Статистика по столбцам:")
    print("{:<15} {:<10} {:<15}".format("Поле", "Заполнено", "Тип данных")) # Выравнивание столбцов для визуального оформления
    print("-" * 40)

    column_stats = defaultdict(list)
    for row in data:
        for i, value in enumerate(row):
            # Обработка пустых полей - считаем пустым если None, пустая строка или строка из пробелов
            cleaned_value = value.strip() if value is not None and value.strip() != '' else None
            column_stats[i].append(cleaned_value)

    for i, header in enumerate(headers):
        values = column_stats[i]
        non_empty = sum(1 for v in values if v != '' and v is not None) # Пустые поля - None или пустая строка

        # Определение типа данных
        is_int = True
        has_data = False  # Есть ли хотя бы одно непустое значение
        for v in values:
            if v is not None and v != '':  # Игнорируем пустые значения
                has_data = True
                if not v.isdigit():
                    is_int = False

        type_name = "int" if is_int and has_data else "string" if has_data else "empty"

        print("{:<15} {:<10} {:<15}".format(header, non_empty, type_name))

Info('ex_for_laba8.csv') # Иногда в столбце "Заполнено" будет встречаться число 12 вместо 13, т.к.
                           # имеются пустые поля для срабатывания функции DelNan

def DelNaN(input_file_path, output_file_path = None):
    if output_file_path is None:
        output_file_path = input_file_path

    with open(input_file_path) as inf:
        headers = next(csv.reader(inf))
        filtered_data = [headers]  # Начинаем с заголовков

        for row in csv.reader(inf):
            if all(value.strip() for value in row):  # Проверяем, что все значения не пустые
                filtered_data.append(row)

    with open(output_file_path, 'w', newline='\n') as outf:              # newline='\n' чтобы не было пробелов между строками в новом файле
        csv.writer(outf, quoting=csv.QUOTE_ALL).writerows(filtered_data) # quoting=csv.QUOTE_ALL чтобы все поля были в кавычках
                                                                         # как и в исходном файле

    print(f"Файл '{input_file_path}' обработан. Пустые строки удалены. Результат записан в '{output_file_path}'.")

# DelNaN('ex_for_laba8.csv', 'DelNan_ex_for_laba8.csv')
# Строки 10, 13, 14 будут удалены, т.к. там есть пустые поля

def MakeDS(input_file_path):
    # Создаем папку workdata и подкаталоги Learning и Testing
    base_dir = 'workdata'
    learning_dir = os.path.join(base_dir, 'Learning')
    testing_dir = os.path.join(base_dir, 'Testing')

    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    with open(input_file_path) as f:
        headers = next(csv.reader(f))  # Считываем заголовки
        data = list(csv.reader(f))     # Считываем остальные строки

    random.shuffle(data) # Перемешиваем данные

    # Определяем количество строк для новых файлов
    total_rows = len(data)
    train_size = int(total_rows * 0.7)

    train_data = data[:train_size]
    test_data = data[train_size:]

    with open(os.path.join(learning_dir, 'train.csv'), 'w', newline='') as train_file:
        csv.writer(train_file, quoting=csv.QUOTE_ALL).writerow(headers)      # Записываем заголовки
        csv.writer(train_file, quoting=csv.QUOTE_ALL).writerows(train_data)  # Записываем данные

    with open(os.path.join(testing_dir, 'test.csv'), 'w', newline='') as test_file:
        csv.writer(test_file, quoting=csv.QUOTE_ALL).writerow(headers)
        csv.writer(test_file, quoting=csv.QUOTE_ALL).writerows(test_data)

    print(f"70% данных из файла ex_for_laba8.csv записаны в '{os.path.join(learning_dir, 'train.csv')}'.")
    print(f"30% данных из файла ex_for_laba8.csv записаны в '{os.path.join(testing_dir, 'test.csv')}'.")

# MakeDS('ex_for_laba8.csv')