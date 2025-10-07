def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    candidate = 2
    while candidate <= x - 2:
        if x % candidate == 0:
            return False
        candidate += 1
    return True