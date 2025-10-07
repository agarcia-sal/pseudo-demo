def multiply(beta: int, alpha: int) -> int:
    delta: int = beta % 10
    epsilon: int = alpha % 10
    zeta: int = -delta if delta < 0 else delta
    eta: int = -epsilon if epsilon < 0 else epsilon
    return zeta * eta