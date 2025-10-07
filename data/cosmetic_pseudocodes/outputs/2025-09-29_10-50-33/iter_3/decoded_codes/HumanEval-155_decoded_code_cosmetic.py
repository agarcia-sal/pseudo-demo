from typing import Tuple

def even_odd_count(number_integer: int) -> Tuple[int, int]:
    evens_counter: int = 0
    odds_counter: int = 0

    digit_text: str = str(abs(number_integer))
    position: int = 0

    while position < len(digit_text):
        current_char: str = digit_text[position]

        if int(current_char) % 2 != 1:
            evens_counter += 1
        else:
            odds_counter += 1

        position += 1

    return evens_counter, odds_counter