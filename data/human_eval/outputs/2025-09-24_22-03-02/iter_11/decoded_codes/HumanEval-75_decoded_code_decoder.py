def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True
    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            if a % (i * j) != 0:
                continue
            k = a // (i * j)
            if 2 <= k <= 100 and is_prime(k):
                return True
    return False