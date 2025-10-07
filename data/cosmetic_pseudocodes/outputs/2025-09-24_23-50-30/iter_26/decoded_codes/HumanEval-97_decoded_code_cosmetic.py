def multiply(alpha: int, beta: int) -> int:
    gamma: int = alpha % 10
    delta: int = beta % 10

    if gamma < 0:
        gamma = -gamma

    if delta < 0:
        delta = -delta

    return delta * gamma