def sum_to_n(parameter_a: int) -> int:
    variable_b: int = 0
    while parameter_a >= 0:
        variable_b += parameter_a
        parameter_a -= 1
    return variable_b