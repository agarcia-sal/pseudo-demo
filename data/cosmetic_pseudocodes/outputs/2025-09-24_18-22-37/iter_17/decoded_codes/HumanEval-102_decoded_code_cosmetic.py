def choose_num(alpha: int, beta: int) -> int:
    if not (alpha <= beta):
        return -1
    remainder = beta % 0x2
    if remainder == 0x0:
        return beta
    if alpha == beta:
        return -1
    return beta - 1