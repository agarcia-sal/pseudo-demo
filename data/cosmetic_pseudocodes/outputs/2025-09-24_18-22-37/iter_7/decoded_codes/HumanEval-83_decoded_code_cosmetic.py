def starts_one_ends(number_m: int) -> int:
    if number_m == 1:
        return 1
    base_val: int = 10
    exponent_val: int = number_m - 2
    power_result: int = base_val ** exponent_val
    final_value: int = 18 * power_result
    return final_value