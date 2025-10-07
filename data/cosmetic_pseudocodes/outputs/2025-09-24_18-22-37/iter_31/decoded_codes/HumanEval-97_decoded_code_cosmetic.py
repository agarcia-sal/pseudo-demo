def multiply(alpha: int, beta: int) -> int:
    gamma: int = alpha % 10
    if gamma < 0:
        gamma = -gamma

    delta: int = beta % 10
    if delta < 0:
        delta = -delta

    epsilon: int = gamma
    zeta: int = delta
    eta: int = epsilon * zeta
    return eta