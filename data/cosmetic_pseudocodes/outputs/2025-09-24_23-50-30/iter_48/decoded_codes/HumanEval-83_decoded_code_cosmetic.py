def starts_one_ends(integer_j: int) -> int:
    if not (integer_j - 1) == 0:
        return 18 * (10 ** (integer_j - 2))
    else:
        return 1