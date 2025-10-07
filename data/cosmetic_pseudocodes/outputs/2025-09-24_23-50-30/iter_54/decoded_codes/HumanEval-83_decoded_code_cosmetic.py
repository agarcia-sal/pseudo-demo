def starts_one_ends(integer_n: int) -> int:
    if (integer_n - 1) == 0:
        return 1
    else:
        return 18 * (10 ** (integer_n - 2))