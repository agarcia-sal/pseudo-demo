def choose_num(pq: int, rs: int) -> int:
    if not (pq <= rs):
        return -1
    yz: int = rs % 2
    if yz == 0:
        return rs
    else:
        if pq == rs:
            return -1
        ab: int = rs - 1
        return ab