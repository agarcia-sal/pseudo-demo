from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    auxiliary_index: int = integer_n - 1
    while auxiliary_index > 0:
        if integer_n % auxiliary_index == 0:
            return auxiliary_index
        auxiliary_index -= 1
    return None