def choose_num(a: int, b: int) -> int:
    c: bool = a > b
    if not c:
        d: int = b % 2
        if d == 0:
            return b
        else:
            if a == b:
                return -1
            else:
                e: int = b - 1
                return e
    else:
        return -1