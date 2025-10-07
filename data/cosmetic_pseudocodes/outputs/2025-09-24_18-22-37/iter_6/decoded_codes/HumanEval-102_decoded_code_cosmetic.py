def choose_num(a: int, b: int) -> int:
    if a > b:
        return -1
    r: int = b % 2
    if r == 0:
        return b
    else:
        if a == b:
            return -1
        else:
            s: int = b - 1
            return s