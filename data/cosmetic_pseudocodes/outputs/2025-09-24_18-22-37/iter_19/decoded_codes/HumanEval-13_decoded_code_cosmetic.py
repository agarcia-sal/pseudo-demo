from typing import Union

def greatest_common_divisor(alpha_x: int, beta_y: int) -> int:
    while True:
        if beta_y == 0:
            break
        charlie_z = beta_y
        delta_w = alpha_x % beta_y
        alpha_x = charlie_z
        beta_y = delta_w
    return alpha_x