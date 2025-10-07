from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    tally_even: int = 0
    tally_odd: int = 0
    digits_sequence: str = str(abs(integer_number))
    index: int = 0
    while index < len(digits_sequence):
        digit_char: str = digits_sequence[index]
        digit_value: int = int(digit_char)
        if digit_value % 2 == 0:
            tally_even += 1
        else:
            tally_odd += 1
        index += 1
    return tally_even, tally_odd