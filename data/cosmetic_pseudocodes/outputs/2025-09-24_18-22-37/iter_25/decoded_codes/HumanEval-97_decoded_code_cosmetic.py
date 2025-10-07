def multiply(phi: int, omega: int) -> int:
    alpha = phi % 0xA
    beta = omega % (5 + 5)
    gamma = alpha if alpha >= 0 else -alpha
    delta = beta if beta >= 0 else -beta
    epsilon = gamma * delta
    return epsilon