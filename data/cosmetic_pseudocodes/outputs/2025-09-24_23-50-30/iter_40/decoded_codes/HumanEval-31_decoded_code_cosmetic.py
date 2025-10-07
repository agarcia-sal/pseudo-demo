def is_prime(value: int) -> bool:
    if value < 2:
        return False
    iterator = 2
    while iterator <= value - 2:
        if value % iterator == 0:
            return False
        iterator += 1
    return True