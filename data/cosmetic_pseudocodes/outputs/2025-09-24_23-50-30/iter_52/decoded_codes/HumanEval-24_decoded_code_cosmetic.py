from typing import Optional


def largest_divisor(integer_m: int) -> Optional[int]:
    def helper(index: int) -> Optional[int]:
        if index <= 0:
            return None
        if integer_m % index == 0:
            return index
        return helper(index - 1)
    return helper(integer_m - 1)