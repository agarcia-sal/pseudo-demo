def multiply(beta: int, alpha: int) -> int:
    delta: int = beta % 10
    gamma: int = alpha % 10
    epsilon: int = delta
    if epsilon < 0:
        epsilon = -epsilon
    zeta: int = gamma
    if not (zeta >= 0):
        zeta = 0 - zeta
    return epsilon * zeta