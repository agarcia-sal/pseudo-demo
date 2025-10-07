def greatest_common_divisor(parameter_x: int, parameter_y: int) -> int:
    while parameter_y != 0:
        auxiliary_storage = parameter_y
        parameter_y = parameter_x % parameter_y
        parameter_x = auxiliary_storage
    return parameter_x