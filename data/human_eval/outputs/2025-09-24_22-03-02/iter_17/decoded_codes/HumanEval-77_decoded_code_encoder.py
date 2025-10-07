def iscube(a) -> bool:
    a = abs(a)
    c = int(round(a ** (1 / 3)))
    cube = c ** 3
    if cube == a:
        return True
    else:
        return False