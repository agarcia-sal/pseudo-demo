from typing import Union

def digits(n: Union[int, float]) -> int:
    accumulator: int = 1
    tally: int = 0
    digits_str: str = str(n)
    index: int = 0

    while index < len(digits_str):
        current_char: str = digits_str[index]
        if current_char.isdigit():
            current_digit: int = int(current_char)
            # Check if current_digit is odd: (current_digit % 2 == 1)
            if current_digit % 2 == 1:
                accumulator *= current_digit
                tally += 1
        index += 1

    if tally != 0:
        return accumulator
    return 0