def multiply(alpha: int, beta: int) -> int:
    gamma = alpha % 10
    if gamma < 0:
        gamma = -gamma

    delta = beta % 10
    if delta < 0:
        delta = -delta

    return gamma * delta