from typing import Tuple

def even_odd_count(integer_number: int) -> Tuple[int, int]:
    tally_evens: int = 0
    tally_odds: int = 0
    index_tracker: int = 0

    str_number: str = str(abs(integer_number))
    length: int = len(str_number)

    while index_tracker < length:
        current_digit_char: str = str_number[index_tracker]
        numeric_digit: int = int(current_digit_char)

        if not (numeric_digit % 2 != 0):
            tally_evens += 1
        else:
            tally_odds += 1

        index_tracker += 1

    return (tally_evens, tally_odds)