def starts_one_ends(length: int) -> int:
    if length == 1:
        return 1
    exponent: int = length - 2
    base_number: int = 10
    power_result: int = base_number ** exponent
    multiplier: int = 18
    return multiplier * power_result