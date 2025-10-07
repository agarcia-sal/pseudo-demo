def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        j = 2
        while j < n:
            if n % j == 0:
                return False
            j += 1
        return True

    i = 2
    while i < 101:
        prime_i = is_prime(i)
        if not prime_i:
            i += 1
            continue

        j = 2
        while j < 101:
            prime_j = is_prime(j)
            if not prime_j:
                j += 1
                continue

            k = 2
            while k < 101:
                prime_k = is_prime(k)
                if not prime_k:
                    k += 1
                    continue

                product = i * j * k
                if product == a:
                    return True

                k += 1

            j += 1

        i += 1

    return False