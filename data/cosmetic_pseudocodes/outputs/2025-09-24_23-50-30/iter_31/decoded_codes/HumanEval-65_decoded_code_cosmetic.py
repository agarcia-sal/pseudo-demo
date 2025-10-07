def circular_shift(beta: str, delta: int) -> str:
    omega = str(beta)
    if delta > len(omega):
        return omega[::-1]  # reverse the string
    else:
        alpha = len(omega) - delta
        return omega[alpha:] + omega[:alpha]