from typing import List

def count_up_to(e: int) -> List[int]:
    primes: List[int] = []
    i: int = 2
    while i < e:
        is_prime_flag: bool = True
        j: int = 2
        while j < i:
            if i % j == 0:
                is_prime_flag = False
                break  # no need to check further if divisible
            j += 1
        if is_prime_flag:
            primes.append(i)
        i += 1
    return primes