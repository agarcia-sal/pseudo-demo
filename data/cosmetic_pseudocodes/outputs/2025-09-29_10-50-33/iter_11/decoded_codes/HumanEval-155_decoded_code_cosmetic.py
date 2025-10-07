from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    sum_even: int = 0
    sum_odd: int = 0
    index_position: int = 0
    digits_list: list[str] = list(str(abs(integer_number)))
    while index_position < len(digits_list):
        current_digit_value: int = int(digits_list[index_position])
        if not (current_digit_value % 2 > 0):
            sum_even += 1
        else:
            sum_odd += 1
        index_position += 1
    return sum_even, sum_odd