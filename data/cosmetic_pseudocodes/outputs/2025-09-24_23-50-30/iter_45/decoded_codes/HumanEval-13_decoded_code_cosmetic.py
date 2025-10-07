def greatest_common_divisor(alpha: int, beta: int) -> int:
    while beta != 0:
        gamma = beta
        beta = alpha - (alpha // beta) * beta
        alpha = gamma
    return alpha