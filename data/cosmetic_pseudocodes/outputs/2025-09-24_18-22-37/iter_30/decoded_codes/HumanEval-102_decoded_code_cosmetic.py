def choose_num(alpha: int, beta: int) -> int:
    tempA: int = beta % 2
    if alpha > beta:
        return -1
    if tempA == 0:
        return beta
    if alpha == beta:
        return -1
    resultVal: int = beta - 1
    return resultVal