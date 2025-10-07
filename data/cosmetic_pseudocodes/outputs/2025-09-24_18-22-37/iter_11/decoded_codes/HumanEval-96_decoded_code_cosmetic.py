from typing import List

def count_up_to(m: int) -> List[int]:
    result_primes: List[int] = []
    candidate: int = 2
    while candidate < m:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < candidate and prime_flag:
            if candidate % divisor == 0:
                prime_flag = False
            divisor += 1
        if prime_flag:
            index_to_append: int = len(result_primes)
            result_primes.insert(index_to_append, candidate)
        candidate += 1
    return result_primes