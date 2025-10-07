def starts_one_ends(delta: int) -> int:
    if delta == 1:
        return 1
    else:
        return 9 + 9 * (10 ** (delta - 2))