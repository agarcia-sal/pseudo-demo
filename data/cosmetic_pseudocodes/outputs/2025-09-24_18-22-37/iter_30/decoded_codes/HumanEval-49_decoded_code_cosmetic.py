def modp(alpha: int, beta: int) -> int:
    gamma: int = 1
    delta: int = 0
    while delta < alpha:
        epsilon = gamma
        zeta = 2 * epsilon
        gamma = zeta % beta
        delta += 1
    return gamma