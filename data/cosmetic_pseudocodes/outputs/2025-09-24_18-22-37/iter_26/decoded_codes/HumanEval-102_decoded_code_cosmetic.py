def choose_num(a: int, b: int) -> int:
    remainder: int = b % 2
    diff: int = a - b

    if diff > 0:
        return -1
    else:
        if remainder == 0:
            return b
        else:
            if a == b:
                return -1
            else:
                return b - 1