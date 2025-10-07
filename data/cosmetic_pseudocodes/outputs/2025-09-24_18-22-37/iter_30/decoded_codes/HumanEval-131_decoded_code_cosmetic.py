def digits(u: int) -> int:
    acc: int = 1
    tally: int = 0
    str_form: str = str(u)
    idx: int = 0
    while idx < len(str_form):
        sym: str = str_form[idx]
        val: int = int(sym)
        if val % 2 == 1:
            acc *= val
            tally += 1
        idx += 1
    if tally == 0:
        return 0
    else:
        return acc