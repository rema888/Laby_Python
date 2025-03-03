def same_elements_count(list1, list2):
    set1 = set(list1) # Повторяющиеся цифры не будем учитывать несколько раз
    set2 = set(list2)
    count = 0
    for item in set1:
        if item in set2:
            count += 1
    return count

a1 = input("Введите элементы первого списка через пробел: ")
a2 = input("Введите элементы второго списка через пробел: ")
my_list1 = [int(item.strip()) for item in a1.split()]
my_list2 = [int(item.strip()) for item in a2.split()]
print("Количество общих чисел из первого и второго списка:", same_elements_count(my_list1, my_list2))