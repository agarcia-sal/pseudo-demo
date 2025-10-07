def greatest_common_divisor(delta_x: int, theta_y: int) -> int:
    while theta_y != 0:
        auxiliary_z = theta_y
        divider_v = delta_x % theta_y
        delta_x = auxiliary_z
        theta_y = divider_v
    return delta_x