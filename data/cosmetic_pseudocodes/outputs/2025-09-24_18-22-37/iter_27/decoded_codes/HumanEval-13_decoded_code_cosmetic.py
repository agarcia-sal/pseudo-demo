def greatest_common_divisor(delta_x: int, delta_y: int) -> int:
    while delta_y != 0:
        temp_storage = delta_y
        mod_result = delta_x % delta_y
        delta_y = mod_result
        delta_x = temp_storage
    return delta_x