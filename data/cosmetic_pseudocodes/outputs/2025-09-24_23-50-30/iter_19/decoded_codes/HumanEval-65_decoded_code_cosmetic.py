def circular_shift(alpha: object, beta: int) -> str:
    omega: str = str(alpha)
    if len(omega) < beta + 1:
        return "".join(reversed(omega))
    delta: int = len(omega) - beta
    return omega[delta:] + omega[:delta]