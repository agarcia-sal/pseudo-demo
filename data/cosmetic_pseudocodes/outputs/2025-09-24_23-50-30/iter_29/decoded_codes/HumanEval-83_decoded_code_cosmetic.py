def starts_one_ends(integer_x: int) -> int:
    integer_y: int = 1
    if integer_x == integer_y:
        return integer_y
    else:
        return 9 * 2 * (10 ** (integer_x - 2))