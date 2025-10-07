def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1
    else:
        if b % 2 != 0:
            if a == b:
                return -1
            else:
                return b - 1
        else:
            return b