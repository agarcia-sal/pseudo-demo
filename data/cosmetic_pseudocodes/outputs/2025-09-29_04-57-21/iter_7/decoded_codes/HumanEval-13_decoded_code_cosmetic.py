def greatest_common_divisor(param_x: int, param_y: int) -> int:
    while param_y != 0:
        aux_var = param_y
        param_y = param_x - (param_x // param_y) * param_y
        param_x = aux_var
    return param_x