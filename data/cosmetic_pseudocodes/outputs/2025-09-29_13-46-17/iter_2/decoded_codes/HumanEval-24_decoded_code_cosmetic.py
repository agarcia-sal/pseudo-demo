from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def find_divisor(current_i: int) -> Optional[int]:
        if current_i == 0:
            return None
        if integer_n % current_i == 0:
            return current_i
        return find_divisor(current_i - 1)

    return find_divisor(integer_n - 1)