dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
print('Заданный словарь - ', dict)
key_input = input('Введите ключ, чьё значение хотите увидеть: ')


if key_input in dict:
    print(dict[key_input])
else:
    print('Такого ключа нет в словаре')