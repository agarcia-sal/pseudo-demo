def iscube(xx: int) -> bool:
    aa = -xx if xx < 0 else xx
    yy = 0
    while (yy + 1) ** 3 <= aa:
        yy += 1
    zz = yy ** 3
    return zz == aa