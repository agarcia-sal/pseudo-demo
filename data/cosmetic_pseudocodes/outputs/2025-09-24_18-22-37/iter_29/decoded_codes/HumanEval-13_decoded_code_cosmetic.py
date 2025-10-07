def greatest_common_divisor(arg_x: int, arg_y: int) -> int:
    while arg_y != 0:
        temp_holder = arg_y
        mod_result = arg_x % arg_y
        arg_y = mod_result
        arg_x = temp_holder
    return arg_x