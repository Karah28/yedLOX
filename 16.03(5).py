import matplotlib.pyplot as plt
import numpy as np
import copy


a_1 = int(input("Введите коэффиценты матрицы:"))
a_2 = int(input("Введите коэффиценты матрицы:"))
a_3 = int(input("Введите коэффиценты матрицы:"))
a_4 = int(input("Введите коэффиценты матрицы:"))
y_1 = int(input("Введите игреки:"))
y_2 = int(input("Введите игреки:"))



matrix = [[a_1, a_2], [a_3, a_4]]


A = (a_1 * a_4) - (a_2 * a_3)



for i in range(1, len(matrix)):
    a_1 = y_1
    a_3 = y_2
    A_1 = (a_1 * a_4) - (a_2 * a_3)
    a_1 = matrix[0][0]
    a_3 = matrix[1][0]
    a_2 = y_1
    a_4 = y_2
    A_2 = (a_1 * a_4) - (a_2 * a_3)
    a_2 = matrix[0][1]
    a_4 = matrix[1][1]

x_1 = A_1 / A
x_2 = A_2 / A

print(x_1, x_2)

x_2 = np.linspace(-5, 5, 100)
x_1 = (6 - 2 * x_2) / 3

plt.plot(x_1, x_2, label='2*x_1 + 3*x_2 = 6')


x_2 = np.linspace(-5, 5, 100)
x_1 = (15 - 4 * x_2) / 9

plt.plot(x_1, x_2, label='4*x_1 + 9*x_2 = 15')

plt.legend()
plt.grid()
plt.show()


