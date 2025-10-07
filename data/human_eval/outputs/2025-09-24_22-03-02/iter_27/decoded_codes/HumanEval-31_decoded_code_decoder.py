def is_prime(n: int) -> bool:
    if n < 2:
        return False
    k = 2
    while k < n - 1:
        if n % k == 0:
            return False
        k += 1
    return True