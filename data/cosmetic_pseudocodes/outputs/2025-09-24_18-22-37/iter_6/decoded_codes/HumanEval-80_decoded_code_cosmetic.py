def is_happy(str_arg: str) -> bool:
    x_len: int = len(str_arg)
    if x_len < 3:
        return False
    pos: int = 0
    while pos <= x_len - 3:
        c1 = str_arg[pos]
        c2 = str_arg[pos + 1]
        c3 = str_arg[pos + 2]
        if not (c1 != c2 and c2 != c3 and c1 != c3):
            return False
        pos += 1
    return True