def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    if beta % 2 == 0:
        return beta
    if not (alpha != beta):
        return -1
    return beta + (-1)