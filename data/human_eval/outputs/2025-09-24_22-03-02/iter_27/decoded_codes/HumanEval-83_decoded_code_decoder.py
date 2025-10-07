def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        power_base = 10
        exponent = n - 2
        power_result = 1
        index = 0
        while index < exponent:
            power_result *= power_base
            index += 1
        result = 18 * power_result
        return result