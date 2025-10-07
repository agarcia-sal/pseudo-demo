from typing import Union


def digits(input_number: int) -> int:
    result_product: int = 1
    count_of_odds: int = 0
    digits_string: str = str(input_number)
    position: int = 0
    while position < len(digits_string):
        current_char: str = digits_string[position]
        numeric_value: int = int(current_char)
        if numeric_value % 2 != 0:
            result_product *= numeric_value
            count_of_odds += 1
        position += 1
    if count_of_odds == 0:
        return 0
    return result_product