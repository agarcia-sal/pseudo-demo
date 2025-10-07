def choose_num(a: int, b: int) -> int:
    if not (a > b):
        if b % 2 == 0:
            return b
        else:
            if a == b:
                return -1
            else:
                return b - 1
    else:
        return -1