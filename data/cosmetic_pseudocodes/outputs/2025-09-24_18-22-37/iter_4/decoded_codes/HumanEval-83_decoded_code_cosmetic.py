def starts_one_ends(num: int) -> int:
    if num == 1:
        return 1
    exponent: int = num - 2
    base: int = 10
    power_result: int = 1
    while exponent > 0:
        power_result *= base
        exponent -= 1
    return 18 * power_result