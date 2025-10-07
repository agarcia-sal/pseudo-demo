def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    if beta % 2 == 0:
        return beta
    else:
        if alpha == beta:
            return -1
        else:
            return beta - 1