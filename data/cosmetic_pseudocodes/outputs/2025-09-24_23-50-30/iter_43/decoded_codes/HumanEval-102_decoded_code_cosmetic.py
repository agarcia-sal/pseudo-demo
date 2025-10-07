def choose_num(p: int, q: int) -> int:
    if not (p <= q):
        return -1
    elif q % 2 == 0:
        return q
    elif p == q:
        return -1
    else:
        return q - 1