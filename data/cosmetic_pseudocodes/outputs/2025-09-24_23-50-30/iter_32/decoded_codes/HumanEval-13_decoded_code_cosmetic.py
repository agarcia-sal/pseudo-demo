from typing import Union

def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            break
        delta = beta
        beta = alpha % delta
        alpha = delta
    return alpha