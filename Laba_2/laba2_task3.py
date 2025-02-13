def number_to_word(n):
    if n < 1 or n > 1000:
        return "Число должно быть в диапазоне от 1 до 1000."

    ones = [
        "", "один", "два", "три", "четыре", "пять",
        "шесть", "семь", "восемь", "девять", "десять",
        "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать","девятнадцать"
    ]

    tens = [
        "", "", "двадцать", "тридцать", "сорок",
        "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
        "девяносто"
    ]

    hundreds = [
        "", "сто", "двести", "триста", "четыреста",
        "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"
    ]

    if n == 1000:
        return "тысяча"

    word = ""

    # Добавление сотен
    if n >= 100:
        word += hundreds[n // 100] + " "
        n %= 100

    # Добавление десятков
    if n >= 20:
        word += tens[n // 10] + " "
        n %= 10

    # Добавление единиц
    if n > 0:
        word += ones[n] + " "

    return word.strip()

x = int(input("Введите число от 1 до 1000: "))
print("Текстовое представление числа:", number_to_word(x))