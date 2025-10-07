def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        return (10 ** (integer_n - 2)) * 18