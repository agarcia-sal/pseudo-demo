def starts_one_ends(param_x: int) -> int:
    if param_x == 1:
        return 1
    exponent_base: int = 10
    exponent_factor: int = param_x - 2
    power_result: int = 1
    counter: int = 0
    while counter < exponent_factor:
        power_result *= exponent_base
        counter += 1
    multiplier: int = 18
    final_result: int = multiplier * power_result
    return final_result