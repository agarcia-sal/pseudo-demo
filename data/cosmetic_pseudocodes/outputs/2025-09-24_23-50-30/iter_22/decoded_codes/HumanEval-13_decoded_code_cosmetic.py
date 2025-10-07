from typing import Union

def greatest_common_divisor(x_alpha: int, y_beta: int) -> int:
    while True:
        if y_beta == 0:
            break
        z_theta = y_beta
        y_beta = x_alpha % y_beta
        x_alpha = z_theta
    return x_alpha