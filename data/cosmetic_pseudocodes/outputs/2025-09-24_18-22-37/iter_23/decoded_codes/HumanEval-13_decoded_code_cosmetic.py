def greatest_common_divisor(alpha: int, beta: int) -> int:
    omega = beta
    while omega != 0:
        star = omega
        omega = alpha % omega
        alpha = star
    return alpha