from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    def tally_digits(digits_str: str, index: int, evens_acc: int, odds_acc: int) -> Tuple[int, int]:
        if index == len(digits_str):
            return evens_acc, odds_acc
        current_char = digits_str[index]
        numeric_val = int(current_char)
        if numeric_val % 2 != 0:
            return tally_digits(digits_str, index + 1, evens_acc, odds_acc + 1)
        else:
            return tally_digits(digits_str, index + 1, evens_acc + 1, odds_acc)

    digits_sequence = str(abs(integer_number))
    return tally_digits(digits_sequence, 0, 0, 0)