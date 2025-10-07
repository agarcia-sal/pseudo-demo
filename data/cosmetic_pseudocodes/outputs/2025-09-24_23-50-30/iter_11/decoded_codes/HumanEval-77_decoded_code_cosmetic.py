def iscube(arg: int) -> bool:
    x = arg
    y = -x if x < 0 else x
    z = round(y ** (1 / 3))
    return z * z * z == y