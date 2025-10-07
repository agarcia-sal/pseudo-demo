def is_prime(n: int) -> bool:
    if n < 2:
        return False
    factor = 2
    while factor <= n - 2:
        if n % factor == 0:
            return False
        factor += 1
    return True