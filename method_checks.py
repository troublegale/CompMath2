from equation_functions import *
from system_functions import *
import numpy as np


def check_single_root(eq, a, b):
    f = eq_funcs[eq - 1]
    if f(a) * f(b) > 0:
        return False
    roots = 0
    if f(a) == 0:
        roots += 1
    if f(b) == 0:
        roots += 1
    step = 0.01
    cur_x = a + step
    while cur_x <= b - step:
        if roots > 1:
            return False
        if f(cur_x) == 0:
            roots += 1
            cur_x += step
            continue
        if f(cur_x) * f(cur_x + step) < 0:
            roots += 1
        cur_x += step
    return roots == 1


def check_convergence(system, x, y):
    x1 = x - 0.25
    x2 = x + 0.25
    y1 = y - 0.25
    y2 = y + 0.25
    return check_system_convergence(system, x1, x2, y1, y2)


def __get_min_max(f, a, b):
    x = np.linspace(a, b, 200)
    y = f(x)
    return np.min(y), np.max(y)


def check_system_convergence(system, x1, x2, y1, y2):
    phi1_dx = max(abs(i) for i in __get_min_max(sys_funcs[system - 1][0], x1, x2))
    phi1_dy = max(abs(i) for i in __get_min_max(sys_funcs[system - 1][1], y1, y2))
    check1 = phi1_dx + phi1_dy < 1
    if not check1:
        return False
    phi2_dx = max(abs(i) for i in __get_min_max(sys_funcs[system - 1][2], x1, x2))
    phi2_dy = max(abs(i) for i in __get_min_max(sys_funcs[system - 1][3], y1, y2))
    check2 = phi2_dx + phi2_dy < 1
    return check2


eq_funcs = [f1, f2, f3]
sys_funcs = [[system1_phi1_dx, system1_phi1_dy, system1_phi2_dx, system1_phi2_dy],
             [system2_phi1_dx, system2_phi1_dy, system2_phi2_dx, system2_phi2_dy]]
