def is_prime(param: int) -> bool:
    if param < 2:
        return False

    for counter in range(2, param - 1):
        if param % counter == 0:
            return False

    return True