def starts_one_ends(length_val: int) -> int:
    if length_val == 1:
        return 1
    base_val = 10
    exponent_val = length_val - 2
    power_result = base_val ** exponent_val
    return 18 * power_result