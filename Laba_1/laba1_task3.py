def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)).center(n * 2 + 50))

n = int(input("Введите количество строк: "))
pascal_triangle(n)