def choose_num(alpha: int, beta: int) -> int:
    while True:
        if alpha > beta:
            return -1
        break

    if beta % 2 == 0:
        return beta
    else:
        if alpha == beta:
            return -1
        else:
            delta: int = beta
            epsilon: int = 1
            zeta: int = delta - epsilon
            return zeta