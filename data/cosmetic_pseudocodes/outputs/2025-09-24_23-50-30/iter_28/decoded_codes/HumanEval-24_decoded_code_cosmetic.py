from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    def helper(integer_j: int) -> Optional[int]:
        if integer_j <= 0:
            return None
        if integer_n % integer_j == 0:
            return integer_j
        return helper(integer_j - 1)
    return helper(integer_n - 1)