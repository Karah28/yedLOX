one = int(input("Введите первый член:"))
diff = int(input("Введите разность прогрессии:"))
den = int(input("Введите знаменатель прогрессии:"))
last = int(input("Введите номер последнего членa:"))
choice = int(input("Способ решения: Формула(1) или Цикл(2)"))
if choice == 1:
    a_n = one + ((last - 1) * diff)

    b_n = one + ((last - 1) * diff)

    Summ_a = (one + a_n) * last / 2

    Summ_b = (one * ((den ** last) - 1)) / (den - 1)
    print("Арифметическая прогрессия:", Summ_a)
    print("геометрическая прогрессия:", Summ_b)
elif choice == 2:

    summ = 0
    s = one
    for i in range(0, last):
        summ = summ + s
        s += diff

    print("Арифметическая прогрессия:", summ)

    summ = 0
    s = one
    for i in range(0, last):
        summ = s + summ
        s *= den

    print("Геометрическая прогрессия:", summ)











