from typing import List

def count_up_to(limit: int) -> List[int]:
    prime_numbers: List[int] = []
    current_number: int = 2
    while current_number < limit:
        prime_flag: bool = True
        divisor_candidate: int = 2
        while divisor_candidate < current_number and prime_flag:
            if current_number % divisor_candidate == 0:
                prime_flag = False
            divisor_candidate += 1
        if prime_flag:
            prime_numbers.append(current_number)
        current_number += 1
    return prime_numbers