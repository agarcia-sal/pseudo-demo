def starts_one_ends(magnitude: int) -> int:
    if magnitude != 1:
        exponent_base: int = 10
        exponent_value: int = magnitude - 2
        power_result: int = 1
        counter: int = 0
        while counter < exponent_value:
            power_result *= exponent_base
            counter += 1
        interim_result: int = 18 * power_result
        return interim_result
    else:
        return 1