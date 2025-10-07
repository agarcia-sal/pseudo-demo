def choose_num(a1: int, b2: int) -> int:
    if a1 > b2:
        return -1
    elif b2 % 2 == 0:
        return b2
    elif a1 == b2:
        return -1
    else:
        return b2 - 1