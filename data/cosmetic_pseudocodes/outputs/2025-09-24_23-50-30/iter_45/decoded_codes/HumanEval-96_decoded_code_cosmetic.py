from typing import List

def count_up_to(n: int) -> List[int]:
    accumulator: List[int] = []
    current: int = 2
    while current < n:
        prime_flag: int = 1
        divisor: int = 2
        while divisor < current and prime_flag == 1:
            if current % divisor == 0:
                prime_flag = 0
            divisor += 1
        if prime_flag == 1:
            accumulator.append(current)
        current += 1
    return accumulator