def starts_one_ends(integer_n: int) -> int:
    if integer_n != 1:
        exponent: int = integer_n - 2
        result: int = 18 * (10 ** exponent)
        return result
    else:
        return 1