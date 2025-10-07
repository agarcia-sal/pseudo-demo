from typing import SupportsIndex

def greatest_common_divisor(alpha: int, beta: int) -> int:
    while beta != 0:
        delta = beta
        beta = alpha - (alpha // beta) * beta
        alpha = delta
    return alpha