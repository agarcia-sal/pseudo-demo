def iscube(beta: int) -> bool:
    gamma: int = abs(beta)
    delta: int = gamma
    epsilon: int = 0
    while epsilon <= delta:
        zeta: int = round(delta ** (1 / 3))
        eta: int = zeta * zeta * zeta
        if eta == gamma:
            return True
        epsilon += 1
    return False