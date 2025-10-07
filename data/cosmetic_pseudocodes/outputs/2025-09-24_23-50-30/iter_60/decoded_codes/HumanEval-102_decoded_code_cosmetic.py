def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    elif beta % 2 == 0:
        return beta
    elif alpha == beta:
        return -1
    else:
        return beta - 1