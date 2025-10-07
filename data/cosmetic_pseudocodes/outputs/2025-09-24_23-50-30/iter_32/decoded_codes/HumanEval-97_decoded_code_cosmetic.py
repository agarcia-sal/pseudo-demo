def multiply(alpha: int, beta: int) -> int:
    delta: int = alpha % 10
    epsilon: int = beta % 10
    zeta: int = delta
    if zeta < 0:
        zeta = -zeta
    eta: int = epsilon
    if not (eta >= 0):
        eta = -eta
    return zeta * eta