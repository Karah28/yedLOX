import math
spisok = []
a = int(input("Введите количество элементов:"))
for i in range(0, a):
    b = int(input("Введите число:"))
    spisok.append(b)
max_int = spisok[0]
for i in range(1, a):
    if spisok[i] > max_int:
        max_int = spisok[i]
print("Максимальное значение(Циклом):", max_int)

max_int = max(spisok)
print("Максимальное значение(Функцией):", max_int)

min_int = spisok[0]
for i in range(1, a):
    if spisok[i] < min_int:
        min_int = spisok[i]

print("Минимальное значение(Циклом):", min_int)

min_int = min(spisok)
print("Минимальное значение(Функцией):", min_int)

sred = sum(spisok) / a
print("Среднее значение: ", sred)

search = int(input("Введите искомое значение: "))
index = -1
for i in range(0, a):
    if spisok[i] == search:
        index = i
        break
print("Индекс значения:", index)

qua = 0
for i in range(0, a):
    qua += 1
print("Количество элементов массива(Циклом): ", qua)

qua = len(spisok)
print("Количество элементов массива(Функцией): ", qua)

summa = 0
for i in range(0, a):
    summa += spisok[i]
print("Сумма элементов массива(Циклом): ", summa)

summa = sum(spisok)
print("Сумма элементов массива(Функцией): ", summa)


c = 1
for i in range(0, a):
    c *= spisok[i]
print("Произведение элементов массива(Циклом): ", c)


c = math.prod(spisok)
print("Произведение элементов массива(Функцией): ", c)



