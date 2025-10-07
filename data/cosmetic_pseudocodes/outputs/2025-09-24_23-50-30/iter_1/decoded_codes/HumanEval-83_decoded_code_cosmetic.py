def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        exponent = integer_n - 2
        base = 10
        result = 1
        for _ in range(exponent):
            result *= base
        return 18 * result