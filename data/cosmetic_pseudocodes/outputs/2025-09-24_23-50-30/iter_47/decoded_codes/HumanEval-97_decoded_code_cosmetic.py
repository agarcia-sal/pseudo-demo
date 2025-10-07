def multiply(alpha: int, beta: int) -> int:
    delta: int = alpha % 10
    epsilon: int = beta % 10

    if delta < 0:
        delta = -delta

    if epsilon < 0:
        epsilon = -epsilon

    return delta * epsilon