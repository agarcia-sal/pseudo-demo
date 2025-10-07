def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            break
        gamma = beta
        beta = alpha - (alpha // beta) * beta
        alpha = gamma
    return alpha