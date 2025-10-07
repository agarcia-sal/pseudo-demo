def choose_num(p: int, q: int) -> int:
    if not (p <= q):
        return -1
    else:
        if (q // 2) * 2 == q:
            return q
        else:
            if p == q:
                return -1
            else:
                return q - 1