import numpy as np
import matplotlib.pyplot as plt


x = int(input("Введите число:"))
a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
d = int(input("Введите число:"))
func = int(input("Введите число:"))
step = int(input("Введите число:"))

def line():

    line1 =  a * x + b

def quadr():
    quadr1 = a*x**2 + b*x + c

def cub():
    cub1 =  a*x**3 + b*x**2 + c*x + d

def search():
    x_min = a
    y_min = func(a)
    x_max = a
    y_max = func(a)
    iter = 0
    for x in range(a, b + step, step):
        iter += 1
        y = func(x)
        if y < y_min:
            x_min = x
            y_min = y
        elif y > y_max:
            x_max = x
            y_max = y
    print{"min": (x_min, y_min), "max": (x_max, y_max), "iterations": iter}
def bisection(func, a, b, d):
    i = 0
    while abs(b - a) > d:
        i += 1
        c = (a + b) / 2
        if func(c) == 0:
            return {"root": (c, func(c)), "iterations": i}
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    print{"root": ((a + b) / 2, func((a + b) / 2)), "iterations": i}

plt.plot(line())
plt.legend()
plt.grid()
plt.show()

