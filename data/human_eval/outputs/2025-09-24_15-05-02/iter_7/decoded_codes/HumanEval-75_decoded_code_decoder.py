def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True

    primes = [x for x in range(2, 101) if is_prime(x)]
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False