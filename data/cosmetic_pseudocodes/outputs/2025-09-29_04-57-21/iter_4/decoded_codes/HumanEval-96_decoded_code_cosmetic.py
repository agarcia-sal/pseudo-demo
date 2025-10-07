from typing import List


def count_up_to(limit: int) -> List[int]:
    prime_numbers: List[int] = []
    current_number: int = 2
    while current_number < limit:
        flag_prime: bool = True
        divisor: int = 2
        while divisor < current_number and flag_prime:
            if current_number % divisor == 0:
                flag_prime = False
            else:
                divisor += 1
        if flag_prime:
            prime_numbers.append(current_number)
        current_number += 1
    return prime_numbers