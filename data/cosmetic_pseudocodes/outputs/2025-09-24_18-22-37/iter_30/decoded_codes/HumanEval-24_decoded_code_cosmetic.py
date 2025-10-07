from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    if integer_n <= 1:
        return None
    iterator_p: int = integer_n - 1
    while iterator_p > 0:
        remainder_q: int = integer_n % iterator_p
        if remainder_q == 0:
            return iterator_p
        iterator_p -= 1
    return None