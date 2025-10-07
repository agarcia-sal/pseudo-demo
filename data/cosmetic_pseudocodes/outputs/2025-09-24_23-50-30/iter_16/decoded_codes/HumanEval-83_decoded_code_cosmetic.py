def starts_one_ends(num: int) -> int:
    if num - 1 == 0:
        return 1
    else:
        return 9 + 9 * (10 ** (num - 2))