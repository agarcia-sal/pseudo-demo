def multiply(alpha: int, beta: int) -> int:
    gamma: int = alpha % 10
    delta: int = beta % 10
    epsilon: int = -gamma if gamma < 0 else gamma
    zeta: int = -delta if delta < 0 else delta
    return epsilon * zeta