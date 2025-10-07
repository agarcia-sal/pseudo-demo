def starts_one_ends(count_value: int) -> int:
    if not (count_value != 1):
        return 1
    base_value: int = 10
    exponent_value: int = count_value + (-2)
    power_result: int = base_value ** exponent_value
    return power_result * 18