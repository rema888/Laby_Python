try:
    with open('laba5_file_input_for_task3.txt', 'r') as f:
        children = []
        for line in f:
            parts = line.strip().split()
            if len(parts) != 3:
                raise ValueError("Неверный формат записи. Ожидалось: Фамилия Имя Возраст.")
            surname, name, age_str = parts
            try:
                age = int(age_str)
                children.append((surname, name, age))
            except ValueError:
                raise ValueError("Возраст должен быть целым числом.")

    if not children:
        raise ValueError("Список детей пуст.") # Если во входном файле не было никаких данных

    youngest = min(children, key = lambda x: x[2]) # Ищем минимальный и максимальный возраст
    oldest = max(children, key = lambda x: x[2])

    with open('laba5_file_output1_for_task3.txt', 'w') as f:
        f.write(youngest[0] + " " + youngest[1] + " " + str(youngest[2]))

    with open('laba5_file_output2_for_task3.txt', 'w') as f:
        f.write(oldest[0] + " " + oldest[1] + " " + str(oldest[2]))

except ValueError as e:
    print(f"Ошибка: {e}")
except FileNotFoundError:
    print("Ошибка: Исходный файл не найден.")
else:
    print("Данные о самом младшем и самом старшем ребенке успешно записаны.")