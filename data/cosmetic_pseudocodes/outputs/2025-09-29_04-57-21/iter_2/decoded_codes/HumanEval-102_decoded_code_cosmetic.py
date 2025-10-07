def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1
    if b % 2 == 0:
        return b
    if a == b:
        return -1
    else:
        return b - 1