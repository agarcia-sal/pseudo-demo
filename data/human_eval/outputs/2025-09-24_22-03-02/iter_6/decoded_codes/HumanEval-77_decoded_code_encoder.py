def iscube(a) -> bool:
    a = abs(a)
    cubeRoot = round(a ** (1/3))
    return cubeRoot ** 3 == a