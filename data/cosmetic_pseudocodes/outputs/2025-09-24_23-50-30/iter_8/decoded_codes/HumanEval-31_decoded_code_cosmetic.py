def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    for counter in range(2, value - 1):
        if value % counter == 0:
            return False
    return True