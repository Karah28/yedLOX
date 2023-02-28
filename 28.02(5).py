import matplotlib.pyplot as plt
import numpy as np

x_min = int(input("Мин. X:"))
x_max = int(input("Макс. X:"))
x_min = x_min - 1
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
x = []
y = []
while x_min != x_max:
    x_min = x_min + 1
    x.append(x_min)
    y = (a * (x_min) ** 2) + (b * (x_min) + c)
    y.append(y)

    print("Координаты x =", x_min, ",y =", y)

plt.plot([x, y])
plt.show()




