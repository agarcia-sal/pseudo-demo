def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power_result = 1
        for _ in range(exponent):
            power_result *= 10
        return 18 * power_result