try:
    with open('laba5_file_input_for_task1.txt', 'r') as f:
        numbers = list(map(float, f.read().strip().split()))
        print(numbers)
        if len(numbers) != 10:
            raise ValueError("Файл должен содержать ровно 10 чисел.")
        mult = 1
        for number in numbers:
            mult *= number

        with open('laba5_file_output_for_task1.txt', 'w') as f:
            f.write(str(mult))

except ValueError as e:
    print(f"Ошибка: {e}") # Если в файле находятся не только числа
except FileNotFoundError:
    print("Ошибка: Файл laba5_file_input_for_task1.txt не найден.")
else:
    print("Произведение чисел записано в файл laba5_file_output_for_task1.txt.")