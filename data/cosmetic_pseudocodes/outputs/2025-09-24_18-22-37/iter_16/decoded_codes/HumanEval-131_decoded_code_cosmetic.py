def digits(m: int) -> int:
    accumulator: int = 1
    tally: int = 0
    str_num: str = str(m)
    pos: int = 0
    while pos < len(str_num):
        ch: str = str_num[pos]
        val: int = int(ch)
        if val % 2 == 1:
            accumulator *= val
            tally += 1
        pos += 1
    if tally == 0:
        return 0
    return accumulator