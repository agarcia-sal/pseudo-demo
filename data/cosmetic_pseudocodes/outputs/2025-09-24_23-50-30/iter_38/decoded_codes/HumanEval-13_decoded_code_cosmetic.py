from typing import SupportsIndex

def greatest_common_divisor(alpha: int, beta: int) -> int:
    if beta == 0:
        return alpha
    else:
        return greatest_common_divisor(beta, alpha - (alpha // beta) * beta)