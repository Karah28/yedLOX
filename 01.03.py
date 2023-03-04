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
    for i in range(one, last + 1):
        s = i + diff
        summ = s + summ
    print("Арифметическая прогрессия:", summ)


    summ = one
    for i in range(one, last + 1):
        s = i * den
        summ = s + summ
    print("геометрическая прогрессия:", summ)











