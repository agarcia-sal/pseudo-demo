def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta == 0:
            break
        delta = beta
        beta = alpha % beta
        alpha = delta
    return alpha