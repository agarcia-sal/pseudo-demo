def is_prime(n):
    if n < 2:
        return False
    k = 2
    while k <= n - 2:
        remainder = n % k
        if remainder == 0:
            return False
        k += 1
    return True