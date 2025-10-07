from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def find_divisor(index_x: int) -> Optional[int]:
        if index_x == 0:
            return None
        if integer_n % index_x == 0:
            return index_x
        return find_divisor(index_x - 1)

    return find_divisor(integer_n - 1)