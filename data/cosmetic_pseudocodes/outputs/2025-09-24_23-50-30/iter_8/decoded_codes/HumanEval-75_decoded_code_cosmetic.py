from typing import List


def is_multiply_prime(a: int) -> bool:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        p = 2
        while p <= x - 1:
            if x % p == 0:
                return False
            p += 1
        return True

    primes_list: List[int] = [candidate for candidate in range(2, 101) if is_prime(candidate)]

    for index_a in range(len(primes_list)):
        for index_b in range(len(primes_list)):
            for index_c in range(len(primes_list)):
                if primes_list[index_a] * primes_list[index_b] * primes_list[index_c] == a:
                    return True

    return False