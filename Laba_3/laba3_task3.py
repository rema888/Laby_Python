def count_string_repeats(list):
    count_dict = {}
    for s in list:
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1

    # Список для хранения результатов в порядке появления строк
    result = []
    for s in list:
        if s in count_dict:
            result.append(count_dict[s])
            del count_dict[s]  # Удаляем, чтобы не дублировать в выводе

    return result

a = input("Введите строки через пробел: ")
my_list = [str(x.strip()) for x in a.split()]
print("Количество повторений строк в порядке их появления в списке:", count_string_repeats(my_list))

# Входные данные из условия задачи
data1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
data2 = ['aaa', 'bbb', 'ccc']
data3 = ['abc', 'abc', 'abc']

print(count_string_repeats(data1))  # [3, 1, 2, 1]
print(count_string_repeats(data2))  # [1, 1, 1]
print(count_string_repeats(data3))  # [3]
