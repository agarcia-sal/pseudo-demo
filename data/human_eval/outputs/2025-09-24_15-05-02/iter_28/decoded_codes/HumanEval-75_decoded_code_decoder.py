from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for j in range(3, int(n**0.5) + 1, 2):
            if n % j == 0:
                return False
        return True

    if a < 8:  # smallest product of three primes >= 2*2*2 = 8
        return False

    primes = [i for i in range(2, 101) if is_prime(i)]

    for i in primes:
        if i > a:
            break
        for j in primes:
            prod_ij = i * j
            if prod_ij > a:
                break
            for k in primes:
                prod = prod_ij * k
                if prod == a:
                    return True
                if prod > a:
                    break
    return False