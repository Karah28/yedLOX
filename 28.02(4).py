x_min = int(input("Мини. X:"))
x_max = int(input("Макс. X:"))
x_min = x_min - 1
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

while x_min != x_max:
    x_min = x_min + 1
    y = (a * (x_min) ** 2) + (b * (x_min) + c)
    print("Координаты x =", x_min, ",y =", y)



