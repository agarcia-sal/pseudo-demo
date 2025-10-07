def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent = n - 2
        power_result = 1
        counter = 1
        while counter <= exponent:
            power_result *= 10
            counter += 1
        result = 18 * power_result
        return result