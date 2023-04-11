import matplotlib.pyplot as plt


def linear(x):
    return 2*x + 3


def quadratic(x):
    return x**2 + 4*x + 1


def cubic(x):
    return x**3 - 3*x**2 + 7*x - 2

# Функция для поиска максимума и минимума методом перебора
def find_maxandmin(brd_l, brd_r, func):
    maximum = float('-inf')
    minimum = float('inf')
    mx_i = mn_i = brd_l
    for i in range(brd_l, brd_r+1):
        f = func(i)
        if f > maximum:
            maximum = f
            maximum_i = i
        if f < minimum:
            minimum = f
            minimum_i = i
    return (minimum_i, minimum, maximum_i, maximum)


def find_root_brute(brd_l, brd_r, func):
    step = 0.01
    x = brd_l
    while x <= brd_r:
        if func(x) * func(x + step) <= 0:
            return (x)
        x += step
    return None



def find_root_dich(brd_l, brd_r, func):
    while brd_r - brd_l > 0.001:
        mid = (brd_l + brd_r) / 2

        if func(brd_l) * func(mid) < 0:
            brd_r = mid
        else:
            brd_l = mid


    return (brd_l / 2, brd_r / 2)


brd_l = -10
brd_r = 10


lin_extremum = find_maxandmin(brd_l, brd_r, linear)
lin_root_brute = find_root_brute(brd_l, brd_r, linear)
lin_root_dichotomy = find_root_dich(brd_l, brd_r, linear)


quad_extremum = find_maxandmin(brd_l, brd_r, quadratic)
quad_root_brute = find_root_brute(brd_l, brd_r, quadratic)
quad_root_dichotomy = find_root_dich(brd_l, brd_r, quadratic)


cubic_extremum = find_maxandmin(brd_l, brd_r, cubic)
cubic_root_brute = find_root_brute(brd_l, brd_r, cubic)
cubic_root_dichotomy = find_root_dich(brd_l, brd_r, cubic)


x = list(range(brd_l-1, brd_r+2))
plt.plot(x, [linear(i) for i in x], label='linear', linewidth=2)
plt.plot(x, [quadratic(i) for i in x], label='quadratic', linewidth=2)
plt.plot(x, [cubic(i) for i in x], label='cubic', linewidth=2)


plt.scatter(lin_extremum[0], lin_extremum[1], color='red', s=50, marker='o')
plt.scatter(lin_extremum[2], lin_extremum[3], color='red', s=50, marker='o')

plt.scatter(lin_root_dichotomy[0], 0, color='blue', s=50, marker='x')
plt.scatter(lin_root_dichotomy[1], 0, color='blue', s=50, marker='x')

plt.scatter(quad_extremum[0], quad_extremum[1], color='red', s=50, marker='o')
plt.scatter(quad_extremum[2], quad_extremum[3], color='red', s=50, marker='o')

plt.scatter(quad_root_dichotomy[0], 0, color='blue', s=50, marker='x')
plt.scatter(quad_root_dichotomy[1], 0, color='blue', s=50, marker='x')

plt.scatter(cubic_extremum[0], cubic_extremum[1], color='red', s=50, marker='o')
plt.scatter(cubic_extremum[2], cubic_extremum[3], color='red', s=50, marker='o')

plt.scatter(cubic_root_dichotomy[0], 0, color='blue', s=50, marker='x')
plt.scatter(cubic_root_dichotomy[1], 0, color='blue', s=50, marker='x')

plt.legend(loc='best')
plt.show()