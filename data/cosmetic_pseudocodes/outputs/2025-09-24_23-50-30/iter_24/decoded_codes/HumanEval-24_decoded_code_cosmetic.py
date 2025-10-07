from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    def hunt_divisor(counter: int) -> Optional[int]:
        if counter <= 0:
            return None
        if integer_n % counter == 0:
            return counter
        return hunt_divisor(counter - 1)

    return hunt_divisor(integer_n - 1)