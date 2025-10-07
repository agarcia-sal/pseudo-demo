def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        power = 1
        exponent = n - 2
        index = 0
        while index < exponent:
            power *= 10
            index += 1
        return 18 * power