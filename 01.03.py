one = int(input("Введите первый член:"))
diff = int(input("Введите разность прогрессии:"))
den = int(input("Введите знаменатель прогрессии:"))
last = int(input("Введите номер последний член:"))
choice = int(input("Способ решения: Формула(1) или Цикл(2)"))
if choice == 1:
    Formula()



def Formula():
    a_n = one + (last - 1) * diff

    b_n = one * (diff ** (last - 1))

    Summ_a = ((one + a_n) * last) / 2

    Summ_b = b_n * diff - one / diff - 1
    print(Summ_a)
    print(Summ_b)



