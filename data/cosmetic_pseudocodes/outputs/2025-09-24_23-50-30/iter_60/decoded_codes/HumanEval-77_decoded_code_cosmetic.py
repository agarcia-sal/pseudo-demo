def iscube(alpha: int) -> bool:
    beta: int = abs(alpha)
    gamma: int = round(beta ** (1 / 3))
    delta: int = gamma ** 3
    return delta == beta