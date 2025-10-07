def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1

    delta = beta % 2
    if delta == 0:
        return beta

    if not (alpha != beta):
        return -1

    omega = beta - 1
    return omega