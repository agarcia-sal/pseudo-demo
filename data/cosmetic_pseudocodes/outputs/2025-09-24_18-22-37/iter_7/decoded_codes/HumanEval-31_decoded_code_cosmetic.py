def is_prime(count: int) -> bool:
    if count < 2:
        return False
    divider = 2
    while divider <= count - 2:
        if count % divider == 0:
            return False
        divider += 1
    return True