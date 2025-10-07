def choose_num(x: int, y: int) -> int:
    if x <= y:
        if y % 2 == 0:
            return y
        else:
            return -1 if x == y else y - 1
    return -1