def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power_result = 10 ** exponent
        result = 18 * power_result
        return result