def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    exponent_value = integer_n - 2
    power_result = 1
    while exponent_value > 0:
        power_result *= 10
        exponent_value -= 1
    return 18 * power_result