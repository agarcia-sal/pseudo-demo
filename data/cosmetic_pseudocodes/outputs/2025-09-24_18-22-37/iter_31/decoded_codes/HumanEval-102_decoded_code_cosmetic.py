def choose_num(a: int, b: int) -> int:
    if b % 2 == 0:
        result = b
    elif a > b:
        result = -1
    elif a == b:
        result = -1
    else:
        result = b - 1
    return result