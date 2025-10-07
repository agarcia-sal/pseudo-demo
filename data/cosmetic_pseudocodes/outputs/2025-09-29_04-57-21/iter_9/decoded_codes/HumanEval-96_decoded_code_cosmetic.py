from typing import List


def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []
    current_number: int = 2
    while current_number < n:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < current_number and prime_flag:
            if current_number % divisor == 0:
                prime_flag = False
            divisor += 1
        if prime_flag:
            prime_numbers.append(current_number)
        current_number += 1
    return prime_numbers