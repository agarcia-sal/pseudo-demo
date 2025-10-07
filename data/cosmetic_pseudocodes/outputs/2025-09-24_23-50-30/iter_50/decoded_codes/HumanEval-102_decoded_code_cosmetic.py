def choose_num(x: int, y: int) -> int:
    idx1: int = x
    idx2: int = y
    if not (idx1 <= idx2):
        return -1
    if (idx2 % 2) == 0:
        return idx2
    if idx1 == idx2:
        return -1
    return idx2 - 1