def iscube(a):
    a = abs(a)
    cube_root_approximation = round(a ** (1 / 3))
    return cube_root_approximation ** 3 == a