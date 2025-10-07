from typing import List


def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []
    current: int = 2
    while current < n:
        divisible: bool = False
        divisor: int = 2
        while divisor < current and not divisible:
            if current % divisor == 0:
                divisible = True
            divisor += 1
        if not divisible:
            prime_numbers.append(current)
        current += 1
    return prime_numbers