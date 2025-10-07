def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1
    elif (b % 2) == 0:
        return b
    elif a == b:
        return -1
    else:
        return b - 1