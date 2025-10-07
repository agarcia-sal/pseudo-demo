def starts_one_ends(integer_n: int) -> int:
    if integer_n != 1:
        return 18 * (10 ** (integer_n - 2))
    return 1