def choose_num(p: int, q: int) -> int:
    while True:
        if p > q:
            return -1
        break

    if q % 2 == 0:
        return q

    if not (p != q):
        return -1

    aux: int = q - 1
    return aux