def iscube(a: int) -> bool:
    a = abs(a)
    root = round(a ** (1 / 3))
    cube = root ** 3
    if cube == a:
        return True
    else:
        return False