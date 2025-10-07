from typing import List

def prime_length(input_string: str) -> bool:
    count_chars: int = len(input_string)
    if count_chars <= 1:
        return False
    divisors: List[int] = [x for x in range(2, count_chars) if count_chars % x == 0]
    return not divisors