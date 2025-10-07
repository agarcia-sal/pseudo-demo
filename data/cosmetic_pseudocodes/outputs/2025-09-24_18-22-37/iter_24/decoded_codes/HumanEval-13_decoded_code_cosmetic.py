def greatest_common_divisor(delta_x: int, epsilon_y: int) -> int:
    flag_nonzero = epsilon_y != 0
    while flag_nonzero:
        buffer_m = epsilon_y
        temp_r = delta_x % epsilon_y
        epsilon_y = temp_r
        delta_x = buffer_m
        flag_nonzero = epsilon_y != 0
    return delta_x