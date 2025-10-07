def iscube(a: int) -> bool:
    a = abs(a)
    temp = int(round(a ** (1/3)))
    cube = temp ** 3
    return cube == a