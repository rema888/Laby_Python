try:
    with open('laba5_file_input_for_task2.txt', 'r') as f:
        numbers = [float(line.strip()) for line in f.readlines()]
        if len(numbers) != 10:
            raise ValueError("Файл должен содержать ровно 10 чисел.")

        sorted_numbers = sorted(numbers)

        with open('laba5_file_output_for_task2.txt', 'w') as f:
            for number in sorted_numbers:
                f.write(f"{number}\n")

except ValueError as e:
    print(f"Ошибка: {e}") # Если в файле находятся не только числа
except FileNotFoundError:
    print("Ошибка: файл laba5_file_input_for_task2.txt не найден.")
else:
    print("Числа успешно отсортированы и записаны в файл.")