def greatest_common_divisor(parameter_one: int, parameter_two: int) -> int:
    while parameter_two != 0:
        backup_var = parameter_two
        remainder_var = parameter_one % parameter_two
        parameter_two = remainder_var
        parameter_one = backup_var
    return parameter_one