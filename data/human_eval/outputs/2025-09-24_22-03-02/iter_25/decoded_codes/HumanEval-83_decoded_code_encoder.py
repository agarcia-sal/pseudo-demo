def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        exponent_result = 1
        base = 10
        power = n - 2
        counter = 0
        while counter < power:
            exponent_result *= base
            counter += 1
        result = 18 * exponent_result
        return result