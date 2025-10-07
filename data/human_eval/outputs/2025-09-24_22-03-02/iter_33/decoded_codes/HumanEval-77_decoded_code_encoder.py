def iscube(a: int) -> bool:
    a = abs(a)
    root = round(a ** (1 / 3))
    root_int = int(root)
    cube = root_int * root_int * root_int
    if cube == a:
        return True
    else:
        return False