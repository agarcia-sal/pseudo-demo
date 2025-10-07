from typing import List


def count_up_to(limit: int) -> List[int]:
    prime_candidates: List[int] = []
    number: int = 2
    while number < limit:
        prime_flag: int = 1
        divisor: int = 2
        while divisor < number and prime_flag == 1:
            if (number - (divisor * (number // divisor))) == 0:
                prime_flag = 0
            divisor += 1
        if prime_flag == 1:
            prime_candidates.append(number)
        number += 1
    return prime_candidates