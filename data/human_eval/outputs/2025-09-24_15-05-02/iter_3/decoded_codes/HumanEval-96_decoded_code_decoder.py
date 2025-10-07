def count_up_to(n):
    """
    Returns a list of prime numbers from 2 up to n-1.
    """
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes