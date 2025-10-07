def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for counter in range(2, value):
        if value % counter == 0:
            return False
    return True