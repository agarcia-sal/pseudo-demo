def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    else:
        if beta % 2 == 0:
            return beta
        else:
            if alpha == beta:
                return -1
    delta = beta
    gamma = 1
    theta = delta - gamma
    return theta