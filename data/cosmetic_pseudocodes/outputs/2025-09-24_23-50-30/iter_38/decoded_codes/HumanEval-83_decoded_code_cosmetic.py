def starts_one_ends(integer_delta: int) -> int:
    return 1 if integer_delta == 1 else 18 * 10 ** (integer_delta - 2)