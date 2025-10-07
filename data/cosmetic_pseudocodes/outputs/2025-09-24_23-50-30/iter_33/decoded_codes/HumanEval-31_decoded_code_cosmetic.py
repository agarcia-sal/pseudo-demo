def is_prime(alpha: int) -> bool:
    if alpha <= 1:
        return False
    beta = 2
    while beta <= alpha - 2:
        if alpha % beta == 0:
            return False
        else:
            beta += 1
    return True