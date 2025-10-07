def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            break
        else:
            gamma: int = beta
            beta = alpha % beta
            alpha = gamma
    return alpha