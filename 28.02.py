import matplotlib.pyplot as plt
import numpy as np

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

Discr = b**2 - 4*a*c
print("Дискриминант:", Discr)
if Discr == 0:
    x_1 = -b / (2 * a)
    y_1 = (a * x_1 ** 2) + (b * x_1) + c
    print("x1 = ", x_1)
    print("Координаты x = ",x_1, "y = ", y_1)



elif Discr > 0:
    x_1 = -b + Discr ** (0.5) / (2 * a)
    x_2 = -b - Discr ** (0.5) / (2 * a)
    print("x1 и x2 = ", x_1,x_2)

    y_1 = (a * x_1 ** 2) + (b * x_1) + c
    y_2 = (a * x_2 ** 2) + (b * x_2) + c

    print("Координаты x = ", x_1, "y = ", y_1)
    print("Координаты x = ", x_2, "y = ", y_2)



else:
    print("Нет действительных корней")


