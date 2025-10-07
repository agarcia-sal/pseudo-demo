def is_prime(value: int) -> bool:
    if value < 2:
        return False

    factor: int = 2
    while factor <= value - 2:
        if value % factor == 0:
            return False
        factor += 1

    return True