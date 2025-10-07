def iscube(a) -> bool:
    a = abs(a)
    cubeRoot = int(round(a ** (1/3)))
    return cubeRoot ** 3 == a