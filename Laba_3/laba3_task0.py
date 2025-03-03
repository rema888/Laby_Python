def greater_than_previous(list):
    result = []
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    return result

a = input("Введите элементы списка через пробел: ")
my_list = [int(x.strip()) for x in a.split()]
print("Список из элементов, которые больше предыдущего:", greater_than_previous(my_list))