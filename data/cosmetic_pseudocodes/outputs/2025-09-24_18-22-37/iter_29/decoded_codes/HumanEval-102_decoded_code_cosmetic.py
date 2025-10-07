def choose_num(a: int, b: int) -> int:
    if a <= b:
        if b % 2 != 0:
            if a == b:
                return -1
            else:
                return b - 1
        else:
            return b
    else:
        return -1