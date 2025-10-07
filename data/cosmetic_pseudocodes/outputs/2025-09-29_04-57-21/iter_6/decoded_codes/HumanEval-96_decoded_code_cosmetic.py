from typing import List

def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []
    current: int = 2
    while current < n:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < current and prime_flag:
            if (current - (current // divisor) * divisor) == 0:
                prime_flag = False
            divisor += 1
        if prime_flag:
            prime_numbers.append(current)
        current += 1
    return prime_numbers