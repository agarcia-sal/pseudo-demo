def starts_one_ends(integer_x: int) -> int:
    if integer_x == 1:
        return 1
    else:
        return 9 * 2 * (10 ** (integer_x - 2))