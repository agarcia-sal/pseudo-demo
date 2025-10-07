def choose_num(x: int, y: int) -> int:
    if not (y < x):
        if (y % 2) == 0:
            return y
        elif not (x != y):
            return -1
        else:
            return y - 1
    return -1