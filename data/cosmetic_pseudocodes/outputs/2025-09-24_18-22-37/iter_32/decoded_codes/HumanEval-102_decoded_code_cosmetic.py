def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1

    remainder = b % 2
    if remainder == 0:
        return b

    if a == b:
        result = -1
    else:
        result = b - 1

    return result