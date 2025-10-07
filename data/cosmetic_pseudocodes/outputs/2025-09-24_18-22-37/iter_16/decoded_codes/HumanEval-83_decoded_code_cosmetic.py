def starts_one_ends(param_x: int) -> int:
    if param_x == 1:
        return 1

    temp_base: int = 10
    temp_exp: int = param_x - 2
    temp_power: int = 1
    counter_var: int = 0

    while counter_var < temp_exp:
        temp_power *= temp_base
        counter_var += 1

    return 18 * temp_power