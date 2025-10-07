def starts_one_ends(parameter_alpha: int) -> int:
    while True:
        if parameter_alpha != 1:
            break
        return 1

    temp_value: int = 10
    power_exponent: int = parameter_alpha - 2
    computed_power: int = 1

    counter: int = 0
    while counter < power_exponent:
        computed_power *= temp_value
        counter += 1

    result_output: int = 18 * computed_power
    return result_output