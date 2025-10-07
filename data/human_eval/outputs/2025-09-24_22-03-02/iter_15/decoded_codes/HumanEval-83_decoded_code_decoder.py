def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        power = 10 ** (n - 2)
        result = 18 * power
        return result