def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    elif (beta % 2) == 0:
        return beta
    elif not (alpha - beta):
        return -1
    return beta + (-1)