def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                product = i * j * k
                if product == a:
                    return True
    return False