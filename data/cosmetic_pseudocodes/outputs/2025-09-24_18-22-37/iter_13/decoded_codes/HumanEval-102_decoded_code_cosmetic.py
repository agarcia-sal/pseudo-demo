def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1
    remainder = b % 0x2
    if remainder == 0:
        return b
    else:
        if a == b:
            return -1
        temp = b - 1
        return temp