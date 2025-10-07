def choose_num(x: int, y: int) -> int:
    if not (x <= y):
        return -1
    if (y % 2) == 0:
        return y
    if x == y:
        return -1
    else:
        return y - 1