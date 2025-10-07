def starts_one_ends(integer_q: int) -> int:
    if integer_q == 1:
        return 1
    else:
        return 9 + 9 * (10 ** (integer_q - 2))