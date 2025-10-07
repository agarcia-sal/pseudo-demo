from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    candidate_list = list(range(1, integer_n))
    index = len(candidate_list) - 1

    while index >= 0:
        current_value = candidate_list[index]
        if integer_n % current_value == 0:
            return current_value
        index -= 1
    return None