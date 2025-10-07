def multiply(beta: int, gamma: int) -> int:
    psi: int = beta % 0xA
    omega: int = gamma % 10

    alpha: int = psi
    if alpha < 0:
        alpha = -alpha

    delta: int = omega
    if delta < 0:
        delta = -delta

    epsilon: int = 0
    epsilon = alpha
    epsilon = epsilon * delta

    return epsilon