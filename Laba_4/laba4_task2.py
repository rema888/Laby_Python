dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('Заданный словарь - ', dict)
value_input = input('Введите значение, чей ключ хотите увидеть: ')

if value_input.isdigit():
    value_input = int(value_input)

found_key = None
for key, value in dict.items():
    if value == value_input:
        found_key = key
        break


if found_key is not None:
    print(found_key)
else:
    print('Такого значения нет в словаре')