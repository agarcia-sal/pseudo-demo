def choose_num(a1: int, b2: int) -> int:
    if b2 < a1:
        return -1
    temp_mod = b2 % 2
    if temp_mod == 0:
        return b2
    if a1 == b2:
        return -1
    result = b2 - 1
    return result