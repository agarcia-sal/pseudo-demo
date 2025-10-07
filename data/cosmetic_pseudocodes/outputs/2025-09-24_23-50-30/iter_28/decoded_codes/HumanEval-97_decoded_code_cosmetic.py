def multiply(beta: int, gamma: int) -> int:
    delta: int = beta % 10
    epsilon: int = gamma % 10
    zeta: int = (delta if delta >= 0 else -delta) * (epsilon if epsilon >= 0 else -epsilon)
    return zeta