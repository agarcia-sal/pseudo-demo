def choose_num(x: int, y: int) -> int:
    flagA: bool = x <= y
    flagB: bool = (y % 2) == 0
    flagC: bool = x != y

    if not flagA:
        return -1
    if flagB:
        return y
    if not flagC:
        return -1
    return y - 1