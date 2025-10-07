def starts_one_ends(size_value: int) -> int:
    if size_value == 1:
        return 1
    exponent_base: int = 10
    exponent_value: int = size_value - 2
    power_result: int = 1
    while exponent_value > 0:
        power_result *= exponent_base
        exponent_value -= 1
    return 18 * power_result