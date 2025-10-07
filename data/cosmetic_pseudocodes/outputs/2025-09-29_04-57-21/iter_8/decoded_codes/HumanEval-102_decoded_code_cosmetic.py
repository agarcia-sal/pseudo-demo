def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    if beta % 2 != 1:
        return beta
    if beta != alpha:
        return beta - 1
    return -1