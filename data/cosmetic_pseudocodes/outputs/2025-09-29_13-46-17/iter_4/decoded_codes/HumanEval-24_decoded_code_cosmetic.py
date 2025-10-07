from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def find_divisor(desc_index: int) -> Optional[int]:
        if desc_index <= 0:
            return None
        if integer_n % desc_index != 0:
            return find_divisor(desc_index - 1)
        return desc_index

    return find_divisor(integer_n - 1)