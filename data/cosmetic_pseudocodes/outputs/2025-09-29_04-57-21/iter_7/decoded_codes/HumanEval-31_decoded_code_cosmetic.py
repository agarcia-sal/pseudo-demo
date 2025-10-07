def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for factor in range(2, n - 1):
        if n % factor == 0:
            return False

    return True