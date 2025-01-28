n = int(input("Введите натуральное число: "))

for i in range(n, 0, -1):
    answer = ''.join(str(x) for x in range(1, i+1))
    print(answer)