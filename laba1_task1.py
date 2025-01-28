print("Введите 3 числа: ")
a = float(input())
b = float(input())
c = float(input())

max = a
min = a


if b >= max:
    max = b
if b < min:
    min = b

if c >= max:
    max = c
if c < min:
    min = c

print("Максимальное число:", max)
print("Минимальное число:", min)

