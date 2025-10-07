def is_prime(alpha: int) -> bool:
    if alpha < 2:
        return False
    x = 2
    while x <= alpha - 2:
        if alpha % x == 0:
            return False
        x += 1
    return True