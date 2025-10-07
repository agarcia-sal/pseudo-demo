def modp(alpha: int, beta: int) -> int:
    gamma: int = 1
    delta: int = 0
    while delta < alpha:
        epsilon: int = 2 * gamma
        gamma = epsilon - (epsilon // beta) * beta
        delta += 1
    return gamma