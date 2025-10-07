def greatest_common_divisor(parameter_x: int, parameter_y: int) -> int:
    if parameter_y == 0:
        return parameter_x
    holder: int = parameter_y
    parameter_y = parameter_x - (parameter_x // parameter_y) * parameter_y
    parameter_x = holder
    while parameter_y != 0:
        holder = parameter_y
        parameter_y = parameter_x - (parameter_x // parameter_y) * parameter_y
        parameter_x = holder
    return parameter_x