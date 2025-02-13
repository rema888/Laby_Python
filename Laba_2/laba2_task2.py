from collections import Counter

def most_used_symbols(s):
    s = s.replace(" ", "")
    c = Counter(s)
    return c.most_common(3)

s = input("Введите строку: ")
print("3 наиболее часто встречающихся символа:")
for char, count in most_used_symbols(s):
    print(f"'{char}': {count}") 