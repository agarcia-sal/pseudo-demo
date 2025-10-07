def is_prime(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i <= x - 2:
        if x % i == 0:
            return False
        i += 1
    return True