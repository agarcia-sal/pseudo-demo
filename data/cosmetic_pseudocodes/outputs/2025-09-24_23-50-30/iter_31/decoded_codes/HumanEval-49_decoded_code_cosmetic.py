def modp(alpha: int, beta: int) -> int:
    gamma: int = 1
    delta: int = 0
    while delta < alpha:
        gamma = (gamma * 2) % beta
        delta += 1
    return gamma