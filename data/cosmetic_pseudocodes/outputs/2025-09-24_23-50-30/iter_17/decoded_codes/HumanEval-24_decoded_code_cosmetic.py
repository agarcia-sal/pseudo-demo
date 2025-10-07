from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    number_list = [x for x in range(integer_n - 1, 0, -1)]
    for element in number_list:
        if integer_n % element == 0:
            return element
    return None