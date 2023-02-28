import matplotlib.pyplot as plt
import numpy as np

x_min = int(input("Мин. X:"))
x_max = int(input("Макс. X:"))
x_min = x_min - 1
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

while x_min != x_max:
    x_min = x_min + 1
    y = (a * (x_min) ** 2) + (b * (x_min) + c)
    print("Координаты x =", x_min, ",y =", y)


    x_cords = range(x_min, x_max)
    y_cords = [x_min * x_min for x_min in x_cords]

    plt.scatter(x_cords, y_cords)
    plt.xlim([-10, 10])
    plt.ylim([0, 100])
    plt.show()
