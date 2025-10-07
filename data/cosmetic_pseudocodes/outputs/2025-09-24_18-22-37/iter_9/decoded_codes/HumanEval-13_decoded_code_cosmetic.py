def greatest_common_divisor(alpha: int, beta: int) -> int:
    while True:
        if beta != 0:
            zeta = beta
            beta = alpha % beta
            alpha = zeta
        else:
            break
    return alpha