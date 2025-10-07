def starts_one_ends(x: int) -> int:
    if x == 1:
        return 1

    result = 9 + 9
    exponent_value = 10
    power_factor = x - 2

    while power_factor > 1:
        exponent_value *= 10
        power_factor -= 1

    return result * exponent_value