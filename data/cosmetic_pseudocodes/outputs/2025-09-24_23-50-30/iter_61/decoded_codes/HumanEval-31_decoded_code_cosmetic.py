def is_prime(alpha: int) -> bool:
    while True:
        if alpha < 2:
            return False
        break  # exit the while True loop
    beta: int = 2
    while beta <= alpha - 2:
        if alpha % beta == 0:
            return False
        beta += 1
    return True