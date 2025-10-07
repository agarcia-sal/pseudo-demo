def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1
    elif (b // 2) * 2 == b:
        return b
    elif (a - b) + (b - a) == 0:
        return -1
    else:
        return b - 1