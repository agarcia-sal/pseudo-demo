def x_or_y(alpha: int, beta: int, gamma: int) -> int:
    if not (alpha != 1):
        return gamma

    zeta = 2
    while zeta < (alpha - 1):
        if (alpha % zeta) == 0:
            return gamma
        zeta += 1

    return beta