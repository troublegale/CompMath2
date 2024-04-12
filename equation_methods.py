from equation_functions import *


def __catch_zero(f, a, b):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f((a + b) / 2) == 0:
        return (a + b) / 2
    return "no"


def solve(method, f, a, b, eps):
    if method == 1:
        return half_division(f, a, b, eps)
    elif method == 2:
        return newton(f, a, b, eps)
    return simple_iteration(f, a, b, eps)


def half_division(f, a, b, eps):
    caught = __catch_zero(f, a, b)
    if caught != "no":
        return caught, 0
    x_prev = (a + b) / 2
    if f(a) * f(x_prev) > 0:
        a = x_prev
    else:
        b = x_prev
    x = (a + b) / 2
    it = 1
    while abs(x - x_prev) > eps and it < MAX_ITER:
        if f(a) * f(x) > 0:
            a = x
        else:
            b = x
        x_prev = x
        x = (a + b) / 2
        it += 1
    return x, it


def newton(f, a, b, eps):
    caught = __catch_zero(f, a, b)
    if caught != "no":
        return caught, 0
    x_prev = (a + b) / 2
    df = derivatives[f]
    x = x_prev - f(x_prev) / df(x_prev)
    it = 1
    while abs(x - x_prev) > eps and it < MAX_ITER:
        x_prev = x
        x = x_prev - f(x_prev) / df(x_prev)
        it += 1
    return x, it


def __calc_lambda(df, a, b):
    dfa = abs(df(a))
    dfb = abs(df(b))
    return -1 / max(dfa, dfb)


def simple_iteration(f, a, b, eps):
    caught = __catch_zero(f, a, b)
    if caught != "no":
        return caught, 0
    df = derivatives[f]
    lam = __calc_lambda(df, a, b)
    phi = lambda x: x + lam * f(x)
    dphi = lambda x: 1 + lam * df(x)
    if abs(dphi(a)) > 1 or abs(dphi(b)) > 1:
        return "never"
    x_prev = (a + b) / 2
    x = phi(x_prev)
    it = 1
    while abs(x - x_prev) > eps and it < MAX_ITER:
        x_prev = x
        x = phi(x_prev)
        it += 1
    return x, it


MAX_ITER = 100000
derivatives = {f1: df1, f2: df2, f3: df3}
