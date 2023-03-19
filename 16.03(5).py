import matplotlib.pyplot as plt
import numpy as np


d = 6
d_1 = 9
d_2 = 6
x_1 = d_1 / d
x_2 = d_2 / d
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


