from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    evens = 0
    odds = 0
    digits = str(abs(integer_number))
    for digit_char in digits:
        digit_value = int(digit_char)
        if digit_value % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds