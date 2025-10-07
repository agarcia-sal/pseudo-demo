def iscube(paramA: int) -> bool:
    x = paramA
    if x < 0:
        x = -x
    y = round(x ** (1 / 3))
    z = y * y * y
    w = (z == x)
    return w