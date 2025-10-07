from typing import List

def count_up_to(n: int) -> List[int]:
    discovered_primes: List[int] = []
    current_number = 2

    while current_number < n:
        prime_flag = True
        divisor = 2

        while divisor < current_number and prime_flag:
            if current_number % divisor == 0:
                prime_flag = False
            divisor += 1

        if prime_flag:
            discovered_primes.append(current_number)

        current_number += 1

    return discovered_primes