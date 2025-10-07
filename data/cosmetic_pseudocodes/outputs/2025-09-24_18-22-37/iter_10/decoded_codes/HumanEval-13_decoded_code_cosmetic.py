def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            break
        gamma = beta
        delta = alpha % beta
        alpha = gamma
        beta = delta
    return alpha