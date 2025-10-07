def choose_num(p: int, q: int) -> int:
    if not (p <= q):
        return -1
    if (q % 2) != 1:
        return q
    if not (p != q):
        return -1
    return q - 1