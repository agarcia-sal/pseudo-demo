def circular_shift(delta: object, omega: int) -> str:
    alpha: str = str(delta)
    if omega > len(alpha):
        return alpha[::-1]
    else:
        beta: int = len(alpha) - omega
        gamma: str = alpha[beta:]
        zeta: str = alpha[:beta]
        return gamma + zeta