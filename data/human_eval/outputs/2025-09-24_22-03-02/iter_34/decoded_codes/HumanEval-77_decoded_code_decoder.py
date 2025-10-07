def iscube(a) -> bool:
    a = abs(a)
    cubeRoot = round(a ** (1 / 3))
    cubeRootInteger = int(cubeRoot)
    cube = cubeRootInteger ** 3
    if cube == a:
        return True
    else:
        return False