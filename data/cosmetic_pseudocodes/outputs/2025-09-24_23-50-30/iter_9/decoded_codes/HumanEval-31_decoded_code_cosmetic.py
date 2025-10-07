def is_prime(value: int) -> bool:
    if value <= 1:
        return False

    cursor = 2
    while cursor <= value - 2:
        if value % cursor == 0:
            return False
        cursor += 1

    return True