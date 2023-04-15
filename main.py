# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from matplotlib import pyplot as plt

#аналог range, но для float переменных
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

#получение массива переменных
def f_range_mas(start, stop, step):
    mas = []
    i = start
    while i < stop:
        mas.append(i)
        i += step

    return mas

#получение массива значений y
def get_y(a, b, start, end, h):
    mas = []
    for i in frange(start, end, h):
        mas.append(a * i / (i ** 4 + b))
    return mas

#Кубическая аппроксимаксия
def square_APPROXIMATION(x, y):
    sum_x = sum(x)
    sum_x_2 = sum(x * x)
    sum_x_3 = sum(x * x * x)
    sum_x_4 = sum(x * x * x * x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_xxy = sum(x * x * y)
    res = np.linalg.solve([[x.size, sum_x, sum_x_2], [sum_x, sum_x_2, sum_x_3], [sum_x_2, sum_x_3, sum_x_4]],
                          [sum_y, sum_xy, sum_xxy])
    print("Квадратная аппроксимация: y=" + str(res[0]) + "+" + str(res[1]) + "x+" + str(res[2]) + "x^2")
    plt_y = []
    plt_x = []
    for i in frange(x[0], x[x.size - 1], 0.01):
        plt_x.append(i)
        plt_y.append(res[0] + i * res[1] + i ** 2 * res[2])
    plt.plot(plt_x, plt_y,)
    S = 0
    l = 0
    for i in x:
        S = S + (res[0] + i * res[1] + i ** 2 * res[2] - y[l]) ** 2
        l = l + 1
    print("S=" + str(S))
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ

#Экспоненцияальная аппроксимаксия
def e_APPROXIMATION(x, y):
    sum_x = sum(x)
    sum_x_2 = sum(x * x)
    sum_y = sum(np.log(y))
    sum_xy = sum(x *np.log(y))
    res = np.linalg.solve([[sum_x_2, sum_x], [sum_x, x.size]], [sum_xy, sum_y])
    print("Экспоненциальная аппроксимация: y=e^(" + str(res[0]) + "*x)+" + str(res[1]))
    plt_y = []
    plt_x = []
    for i in frange(x[0], x[x.size - 1], 0.01):
        plt_x.append(i)
        plt_y.append(math.e**(i*res[0]) + res[1])
    plt.plot(plt_x, plt_y, 's')
    S = 0
    l = 0
    for i in x:
        S = S + (math.e**(i*res[0]) + res[1] - y[l]) ** 2
        l = l + 1
    print("S=" + str(S))
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ
#Логарифмическая аппроксимаксия
def log_APPROXIMATION(x, y):
    sum_x = sum(np.log(x))
    sum_x_2 = sum(np.log(x) * np.log(x))
    sum_y = sum(y)
    sum_xy = sum(np.log(x)*y)
    res = np.linalg.solve([[sum_x_2, sum_x], [sum_x, x.size]], [sum_xy, sum_y])
    print("Логарифмическая аппроксимация: y=" + str(res[0]) + "*lnx+" + str(res[1]))
    plt_y = []
    plt_x = []
    for i in frange(x[0], x[x.size - 1], 0.01):
        plt_x.append(i)
        plt_y.append(res[0]*math.log(i) + res[1])
    plt.plot(plt_x, plt_y, 'r')
    S = 0
    l = 0
    for i in x:
        S = S + (res[0]*math.log(i) + res[1] - y[l]) ** 2
        l = l + 1
    print("S=" + str(S))
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ

#Степенная аппроксимаксия
def degree_APPROXIMATION(x, y):
    sum_x = sum(np.log(x))
    sum_x_2 = sum(np.log(x) * np.log(x))
    sum_y = sum(np.log(y))
    sum_xy = sum(np.log(x) * np.log(y))
    res = np.linalg.solve([[sum_x_2, sum_x], [sum_x, x.size]], [sum_xy, sum_y])
    print("Степенная аппроксимация: y=" + str(res[0]) + "*x^" + str(res[1]))
    plt_y = []
    plt_x = []
    for i in frange(x[0], x[x.size - 1], 0.01):
        plt_x.append(i)
        plt_y.append(res[0] * math.pow(i, res[1]))
    plt.plot(plt_x, plt_y, 'b')
    S = 0
    l = 0
    for i in x:
        S = S + (res[0] * math.pow(i, res[1]) - y[l]) ** 2
        l = l + 1
    print("S=" + str(S))
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ

#Кубическая аппроксимаксия
def cube_APPROXIMATION(x, y):
    sum_x = sum(x)
    sum_x_2 = sum(x * x)
    sum_x_3 = sum(x * x * x)
    sum_x_4 = sum(x * x * x * x)
    sum_x_5 = sum(x * x * x * x * x)
    sum_x_6 = sum(x * x * x * x * x * x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_xxy = sum(x * x * y)
    sum_xxxy = sum(x * x * x * y)
    res = np.linalg.solve(
        [[x.size, sum_x, sum_x_2, sum_x_3], [sum_x, sum_x_2, sum_x_3, sum_x_4], [sum_x_2, sum_x_3, sum_x_4, sum_x_5],
         [sum_x_3, sum_x_4, sum_x_5, sum_x_6]],
        [sum_y, sum_xy, sum_xxy, sum_xxxy])
    print("Кубическая аппроксимация: y=" + str(res[0]) + "+" + str(res[1]) + "x+" + str(res[2]) + "x^2+" + str(
        res[3]) + "x^3")
    plt_y = []
    plt_x = []
    for i in frange(x[0], x[x.size - 1], 0.01):
        plt_x.append(i)
        plt_y.append(res[0] + i * res[1] + i ** 2 * res[2] + i ** 3 * res[3])
    S = 0
    l=0
    for i in x:
        S=S+(res[0] + i * res[1] + i ** 2 * res[2] + i ** 3 * res[3]-y[l])**2
        l=l+1
    print("S="+str(S))
    plt.plot(plt_x, plt_y, 'y')
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ


#Линейная аппроксимаксия
def line_APPROXIMATION(x, y):
    sum_x = sum(x)
    sum_x_2 = sum(x * x)
    sum_xy = sum(x * y)
    sum_y = sum(y)
    res = np.linalg.solve([[sum_x_2, sum_x], [sum_x, x.size]], [sum_xy, sum_y])
    print("Линейная аппроксимация: y=" + str(res[0]) + "*x+" + str(res[1]))
    plt.plot([x[0], x[x.size - 1]], [res[0] * x[0] + res[1], res[0] * x[x.size - 1] + res[1]], 'g')
    S = 0
    l = 0
    for i in x:
        S = S + (res[0]* i +res[1] - y[l]) ** 2
        l = l + 1
    print("S=" + str(S))
    σ = (S / x.size) ** 0.5
    print("σ=" + str(σ))
    return σ

if __name__ == '__main__':
    mod = input('C-консольный, F-файловый.\n')
    while mod != "C" and mod != "F":
        mod = input('Не правильно, попробуйте снова.\n')
    x = []
    y = []
    if mod == "C":
        print("Формат функции:f(x)=a*x/(x^4+b)")
        a = float(input('Введите значения a:'))
        b = float(input('Введите значения b:'))
        start = float(input('Начало исследуемого интервала:'))
        end = float(input('Конец исследуемого интервала:'))
        h = float(input('Шаг иcледуемого интервала:'))
        x = np.array(f_range_mas(start, end, h))
        y = np.array(get_y(a, b, start, end, h))
        for i in range(x.size):
            plt.plot(x[i], y[i], 'bs')
        plt.locator_params(axis='x', nbins=25)
    min_σ = 1000000000
    σ_line = line_APPROXIMATION(x, y)
    if σ_line<min_σ:
        min_σ=σ_line
    σ_square = square_APPROXIMATION(x, y)
    if σ_square<min_σ:
        min_σ=σ_square
    σ_cube = cube_APPROXIMATION(x, y)
    if σ_cube<min_σ:
        min_σ=σ_cube
    σ_e = e_APPROXIMATION(x, y)
    if σ_e<min_σ:
        min_σ=σ_e
    σ_log = log_APPROXIMATION(x, y)
    if σ_log<min_σ:
        min_σ=σ_log
    σ_degree = degree_APPROXIMATION(x, y)
    if σ_degree<min_σ:
        min_σ=σ_degree
    print("Наилучшее приближение имеет ", end='')
    if σ_line == min_σ:
        print("линейная аппроксимаксия.")
    elif σ_square == min_σ:
        print("квадратная аппроксимаксия.")
    elif σ_cube == min_σ:
        print("кубическая аппроксимаксия.")
    elif σ_e == min_σ:
        print("экспоненциальная аппроксимаксия.")
    elif σ_log == min_σ:
        print("логарифмическая аппроксимаксия.")
    elif σ_degree == min_σ:
        print("степенная аппроксимаксия.")
    plt.show()
