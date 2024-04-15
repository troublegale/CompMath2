from system_functions import *


def solve_system(system, x0, y0, eps):
    x = phi[system - 1][0](x0, y0)
    y = phi[system - 1][1](x0, y0)
    i = 1
    while abs(x - x0) > eps or abs(y - y0) > eps:
        x0 = x
        y0 = y
        x = phi[system - 1][0](x0, y0)
        y = phi[system - 1][1](x0, y0)
        i += 1
    res = {
        "i": i,
        "x": x,
        "y": y,
    }
    return res


phi = [[system1_phi1, system1_phi2], [system2_phi1, system2_phi2]]
