def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divider = 2
    while divider <= value - 2:
        if value % divider == 0:
            return False
        divider += 1
    return True