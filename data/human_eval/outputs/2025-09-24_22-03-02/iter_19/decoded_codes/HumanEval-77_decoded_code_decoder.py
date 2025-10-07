def iscube(a: int) -> bool:
    a = abs(a)
    cuberoot = round(a ** (1 / 3))
    cuberoot_cube = cuberoot ** 3
    return cuberoot_cube == a