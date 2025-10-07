def choose_num(alpha: int, beta: int) -> int:
    if (alpha <= beta) and (beta % 2 == 0):
        return beta
    if (alpha <= beta) and (beta % 2 != 0) and (alpha == beta):
        return -1
    if alpha > beta:
        return -1
    return beta - 1