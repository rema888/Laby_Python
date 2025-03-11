def dict_with_3_most_common_numbers(s):
    # Преобразуем строку в список чисел
    numbers = [int(num) for num in s if num.isdigit()]

    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    # Сортируем словарь по значениям и берем 3 самых частых
    sorted_counts = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    # Создаем новый словарь для 3 самых частых чисел
    most_common = dict(sorted_counts[:3])
    return most_common

s = input('Введите строку, состоящую из цифр от 0 до 9: ')
print('Словарь из трёх самых часто встречаемых чисел - ', dict_with_3_most_common_numbers(s))