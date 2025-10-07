def greatest_common_divisor(variable_x: int, variable_y: int) -> int:
    if variable_y == 0:
        return variable_x
    return greatest_common_divisor(variable_y, variable_x - (variable_x // variable_y) * variable_y)