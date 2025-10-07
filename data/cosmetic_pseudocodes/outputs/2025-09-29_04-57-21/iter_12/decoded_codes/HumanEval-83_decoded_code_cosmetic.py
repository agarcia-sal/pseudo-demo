def starts_one_ends(count: int) -> int:
    if count == 1:
        return 1
    base_value: int = 10
    exponent: int = count - 2
    power_result: int = base_value ** exponent
    multiplier: int = 18
    return multiplier * power_result