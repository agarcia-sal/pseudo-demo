def is_multiply_prime(a):
    # Check if a given number n is prime
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True

    primes = [i for i in range(2, 101) if is_prime(i)]

    # Check all products of three primes within the range
    for i in primes:
        if i > a:  # Optimization: no need to check if prime greater than 'a'
            break
        for j in primes:
            if i * j > a:  # Optimization to skip unnecessary checks
                break
            for k in primes:
                product = i * j * k
                if product > a:
                    break
                if product == a:
                    return True
    return False