def count_up_to(n):
    primes = []
    i = 2
    while i < n:
        is_prime = True
        j = 2
        while j < i:
            if i % j == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            primes.append(i)
        i += 1
    return primes