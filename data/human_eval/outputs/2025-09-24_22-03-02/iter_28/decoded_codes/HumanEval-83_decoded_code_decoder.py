def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power = 1
        for index in range(1, exponent + 1):
            power *= 10
        result = 18 * power
        return result