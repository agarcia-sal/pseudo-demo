from typing import Union

def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            return alpha
        gamma = beta
        beta = alpha - (alpha // beta) * beta
        alpha = gamma