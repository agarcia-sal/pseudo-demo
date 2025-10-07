def choose_num(x, y):
    if x > y:
        return -1
    remainder = y % 2
    if remainder == 0:
        return y
    if x == y:
        return -1
    return y - 1