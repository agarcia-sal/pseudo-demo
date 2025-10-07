def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power_result = 1
        index = 0
        while index < exponent:
            power_result *= 10
            index += 1
        return 18 * power_result