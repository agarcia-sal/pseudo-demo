def choose_num(alpha: int, beta: int) -> int:
    if alpha == beta:
        return -1
    if beta % 2 == 0:
        return beta
    if alpha > beta:
        return -1
    epsilon = beta - 1
    return epsilon