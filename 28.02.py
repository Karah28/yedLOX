a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

Discr = b**2 - 4*a*c
print("Дискриминант:", Discr)
if Discr == 0:
    x_1 = -b / (2 * a)
    print("x1 = ", x_1)
elif Discr > 0:
    x_1 = -b + Discr ** (0.5) / (2 * a)
    x_2 = -b - Discr ** (0.5) / (2 * a)
    print("x1 и x2 = ", x_1,x_2)
else:
    print("Нет действительных корней")
