def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [p for p in range(2, 101) if is_prime(p)]
    primes_set = set(primes)
    for i in primes:
        if a % i != 0:
            continue
        for j in primes:
            if a % (i * j) != 0:
                continue
            k = a // (i * j)
            if k in primes_set:
                return True
    return False