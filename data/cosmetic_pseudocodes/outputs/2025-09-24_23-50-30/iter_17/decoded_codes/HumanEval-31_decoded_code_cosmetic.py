def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for iterator in range(2, value - 1):
        if value % iterator == 0:
            return False
    return True