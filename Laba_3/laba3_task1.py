def swap_min_max(list):
    if not list:
        return list  # Если список пустой, возвращаем пустой список

    min_index = list.index(min(list))
    max_index = list.index(max(list))

    list[min_index], list[max_index] = list[max_index], list[min_index]
    return list

a = input("Введите элементы списка через пробел: ")
my_list = [int(x.strip()) for x in a.split()]
print("Список, где минимальный и максимальный элемент поменялись местами:", swap_min_max(my_list))