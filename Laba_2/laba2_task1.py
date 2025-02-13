def compress(x):
    if not x: # Проверка на пустую строку
        return ""

    comp = []
    count = 1

    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            count += 1
        else:
            comp.append(x[i - 1])
            if count > 1:
                comp.append(str(count))
            count = 1

    comp.append(x[-1])
    if count > 1:
        comp.append(str(count))

    return ''.join(comp)

s = input("Введите строку, состоящую из латинских букв: ")
print(compress(s))