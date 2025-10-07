def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        j = 2
        while j < n:
            if n % j == 0:
                return False
            j += 1
        return True

    i = 2
    while i <= 101:
        if not is_prime(i):
            i += 1
            continue
        j = 2
        while j <= 101:
            if not is_prime(j):
                j += 1
                continue
            k = 2
            while k <= 101:
                if not is_prime(k):
                    k += 1
                    continue
                if i * j * k == a:
                    return True
                k += 1
            j += 1
        i += 1
    return False