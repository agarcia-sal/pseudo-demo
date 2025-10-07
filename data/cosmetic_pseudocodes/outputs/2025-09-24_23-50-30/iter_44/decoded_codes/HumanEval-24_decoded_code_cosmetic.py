from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def find_divisor(current_x: int) -> Optional[int]:
        if current_x <= 0:
            return None
        if integer_n % current_x == 0:
            return current_x
        return find_divisor(current_x - 1)

    return find_divisor(integer_n - 1)