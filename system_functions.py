from numpy import sin, cos


def system1_equation1(x, y):
    return cos(y + 0.5) - 0.05*x**3 - x - 2


def system1_phi1(x, y):
    return cos(y + 0.5) - 0.05*x**3 - 2


def system1_phi1_dx(x):
    return -0.15*x**2


def system1_phi1_dy(y):
    return -sin(y + 0.5)


def system1_equation2(x, y):
    return -0.1*x**3 - 0.1*y**3 - y - 0.5


def system1_phi2(x, y):
    return -0.1*x**3 - 0.1*y**3 - 0.5


def system1_phi2_dx(x):
    return -0.3*x**2


def system1_phi2_dy(y):
    return -0.3*y**2


def system2_equation1(x, y):
    return sin(0.5*y) - x - 0.2*x**2 + 0.1


def system2_phi1(x, y):
    return sin(0.5*y) - 0.2*x**2 + 0.1


def system2_phi1_dx(x):
    return -0.4*x


def system2_phi1_dy(y):
    return 0.5*sin(0.5*y)


def system2_equation2(x, y):
    return 0.3*x**2 - 0.1*y**3 - y + 0.3


def system2_phi2(x, y):
    return 0.3*x**2 - 0.1*y**3 + 0.3


def system2_phi2_dx(x):
    return 0.6*x


def system2_phi2_dy(y):
    return -0.3*y**2
