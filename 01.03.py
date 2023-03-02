one = int(input("Введите первый член:"))
diff = int(input("Введите разность прогрессии:"))
den = int(input("Введите знаменатель прогрессии:"))
last = int(input("Введите номер последний член:"))
choice = int(input("Способ решения: Формула(1) или Цикл(2)"))
if choice == 1:
    a_n = one + ((last - 1) * diff)

    b_n = one * den ** (last - 1)

    Summ_a = (one + a_n) * last / 2

    Summ_b = (one * ((den ** b_n) - 1)) / (den - 1)
    print("Арифметическая прогрессия:", Summ_a)
    print("геометрическая прогрессия:", Summ_b)
elif choice == 2:

    summ = []
    for i in range(last):
        one = i + one
        diff = one + diff
    print(diff)

    for i in range(last):
         one_a = one * (den ** i)

    print(one_a)











