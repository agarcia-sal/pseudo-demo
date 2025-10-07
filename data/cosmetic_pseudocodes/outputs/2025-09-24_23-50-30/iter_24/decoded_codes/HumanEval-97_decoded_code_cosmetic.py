def multiply(alpha: float, beta: float) -> float:
    gamma: float = alpha - ((alpha / 10) * 10)
    if gamma < 0:
        gamma = -gamma
    delta: float = beta - ((beta / 10) * 10)
    if delta < 0:
        delta = -delta
    return delta * gamma