def digits(q: int) -> int:
    x_prod: int = 1
    tally_odd: int = 0
    str_q: str = str(q)
    idx: int = 0
    while idx < len(str_q):
        ch: str = str_q[idx]
        val_num: int = int(ch)
        if val_num % 2 == 1:
            # multiply product by odd digit and increment tally
            x_prod *= val_num
            tally_odd += 1
        idx += 1
    if tally_odd == 0:
        return 0
    return x_prod