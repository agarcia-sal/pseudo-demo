def solve(alpha: int) -> str:
    beta: int = 0
    gamma: str = str(alpha)
    delta: int = 0
    epsilon: int = len(gamma)
    while delta < epsilon:
        zeta: str = gamma[delta]
        eta: int = int(zeta)
        beta += eta
        delta += 1
    theta: str = bin(beta)
    iota: str = theta[2:]
    return iota