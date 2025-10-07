def choose_num(x: int, y: int) -> int:
    if x > y:
        return -1
    remainder = y % 2
    if remainder == 0:
        return y
    if x == y:
        return -1
    result = y - 1
    return result