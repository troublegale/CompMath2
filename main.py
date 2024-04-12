from method_checks import *
from equation_methods import *
from system_methods import *


# a = 3.5
# b = 5.9
# eps = 0.0000001
# equation = 1
# method = 2
# if check_single_root(equation, a, b):
#     solution = solve(method, equation, a, b, eps)
#     print(f"x={solution[0]}\ndone in {solution[1]} iterations")
# else:
#     print("no roots or more than 1 root")

x0 = -1
y0 = -0.5
eps = 0.0000000001
system = 1
if check_convergence(system, x0, y0):
    solution = solve_system(system, x0, y0, eps)
    print(f"x={solution[0]}\ny={solution[1]}\ndone in {solution[2]} iterations")
else:
    print("system doesn't converge to this initial values.")
