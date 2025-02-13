def decompress(x):
    comp = []
    i = 0

    while i < len(x):
        current_char = x[i]
        i += 1
        count = 0

        while i < len(x) and x[i].isdigit():
            count = count * 10 + int(x[i])
            i += 1

        if count == 0:
            comp.append(current_char)
        else:
            comp.append(current_char * count)

    return ''.join(comp)

s = input("Введите строку, состоящую из латинских букв: ")
print(decompress(s))