import matplotlib.pyplot as plt
import numpy as np
import copy


a_1 = int(input("Введите коэффиценты матрицы:"))
a_2 = int(input("Введите коэффиценты матрицы:"))
b_1 = int(input("Введите игреки:"))
b_2 = int(input("Введите игреки:"))



matrix = [[a_1, a_2], [b_1, b_2]]


d = (a_1 * b_2) - (a_2 * b_1)
d_1 = d + b_2

for i in range(1, len(matrix)):
    matrix_1 = copy.deepcopy(matrix)
    matrix[0][0] = d
    matrix[1][0] = d_1
    matrix_1[0][1] = d
    matrix_1[1][1] = d_1
    print(matrix, matrix_1)

D_1 = d * b_2 - a_2 * d_1
D_2 = d * b_1 - a_1 * b_2

x_1 = D_1 / d
x_2 = D_2 / d

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


