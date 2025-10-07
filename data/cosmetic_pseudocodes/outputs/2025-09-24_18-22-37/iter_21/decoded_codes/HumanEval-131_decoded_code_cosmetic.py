def digits(x: int) -> int:
    mult: int = 1
    tally: int = 0
    str_x: str = str(x)
    idx: int = 0
    while True:
        if idx >= len(str_x):
            break
        ch: str = str_x[idx]
        val: int = int(ch)
        if val % 2 == 1:
            mult *= val
            tally += 1
        idx += 1
    if tally == 0:
        return 0
    return mult