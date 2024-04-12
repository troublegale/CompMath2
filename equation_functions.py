from numpy import sin, cos


def f1(x):
    return x**3 - 3*x**2 - 6*x + 8


def df1(x):
    return 3*x**2 - 6*x - 6


def f2(x):
    return 1/2 * (x - 5) * (x + 1)


def df2(x):
    return x - 2


def f3(x):
    return 6 * sin(5/2 * x) + 3


def df3(x):
    return 15 * cos(5/2 * x)
