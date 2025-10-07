from typing import List


def count_up_to(n: int) -> List[int]:
    primes_collection: List[int] = []
    index: int = 2
    while index < n:
        prime_flag: int = 1
        divisor: int = 2
        while divisor < index and prime_flag == 1:
            if not ((index % divisor) != 0):
                prime_flag = 0
            divisor += 1
        if prime_flag != 0:
            primes_collection.append(index)
        index += 1
    return primes_collection