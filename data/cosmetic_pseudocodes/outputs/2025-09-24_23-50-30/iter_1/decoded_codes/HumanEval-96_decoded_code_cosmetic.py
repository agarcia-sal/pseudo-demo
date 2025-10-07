from typing import List

def count_up_to(n: int) -> List[int]:
    primes: List[int] = []
    current: int = 2
    while current < n:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < current and prime_flag:
            if current % divisor == 0:
                prime_flag = False
            divisor += 1
        if prime_flag:
            primes.append(current)
        current += 1
    return primes