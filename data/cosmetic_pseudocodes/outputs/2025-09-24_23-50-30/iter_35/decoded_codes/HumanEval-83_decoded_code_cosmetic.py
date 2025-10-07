def starts_one_ends(integer_p: int) -> int:
    if integer_p == 1:
        return 1
    return (10 ** (integer_p - 2)) * 18